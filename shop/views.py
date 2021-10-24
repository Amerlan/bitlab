from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from rest_framework.viewsets import ModelViewSet
from .permissions import IsCustomer


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


