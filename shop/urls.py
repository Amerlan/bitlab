from django.urls import path

from .views import IndexView, ProductView, ProductDetailView, OrderView

shop_urlpatterns = [
    # path('', IndexView.as_view()),
    path('api/products/', ProductView.as_view()),
    path('api/orders/<int:pk>/', OrderView.as_view()),
    path('products/<int:pk>/', ProductDetailView.as_view()),
]
