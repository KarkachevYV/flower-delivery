# catalog/urls.py 
from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('flower-catalog/', views.flower_catalog, name='flower_catalog'),  # каталог цветов
    # path('cart/', views.cart_views, name='cart'),
    # path('add-to-cart/<int:flower_id>/', views.add_to_cart, name='add_to_cart'),
    path('api/flowers/', views.FlowerViewSet.as_view({'get': 'list'}), name='flower_api'),  # API для получения цветов
]