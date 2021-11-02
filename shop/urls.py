from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ProductViewSet, SendEmailViewSet


router = DefaultRouter()
router.register('products', ProductViewSet)


shop_urlpatterns = [
    path('', include(router.urls)),
    path('send-email/', SendEmailViewSet.as_view({'post': 'send_email'})),
]
