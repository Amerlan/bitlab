from django.contrib import admin
from django.urls import path, include
from shop.urls import shop_urlpatterns
from .swagger import urlpatterns as swagger_urlpatterns
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(swagger_urlpatterns)),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

urlpatterns += shop_urlpatterns
