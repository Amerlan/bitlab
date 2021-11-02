from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import Product
from .permissions import IsCustomer
from .serializers import ProductSerializer, EmailSerializer
from .tasks import send_email


class IndexView(APIView):
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'create_product.html'
    permission_classes = (AllowAny, )

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        context = {
            'products': serializer.data
        }
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        product = Product.objects.create(**data)
        serializer = ProductSerializer(product)
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, IsCustomer)


class SendEmailViewSet(GenericViewSet):
    serializer_class = EmailSerializer
    permission_classes = (AllowAny, )

    def send_email(self, request):
        serializer = EmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        send_email.delay(**serializer.validated_data)
        return Response(status=status.HTTP_200_OK)

