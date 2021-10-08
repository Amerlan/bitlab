from django.contrib import admin
from django.urls import path, include
from shop.urls import shop_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += shop_urlpatterns
