from django.urls import path
from .views import \
    load_page_create_product,\
    create_product,\
    login_view,\
    logout_view, show_users

shop_urlpatterns = [
    path('product/', load_page_create_product),
    path('create-product/', create_product, name="creation"),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('show_users/', show_users),
]
