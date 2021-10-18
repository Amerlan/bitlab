from django.urls import path

from .views import IndexView
# from .views import \
#     load_page_create_product,\
#     create_product,\
#     login_view,\
#     logout_view

shop_urlpatterns = [
    path('', IndexView.as_view()),
    # path('product/', load_page_create_product),
    # path('create-product/', create_product, name="creation"),
    # path('login/', login_view, name='login'),
    # path('logout/', logout_view, name='logout')
