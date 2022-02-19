from django.urls import path, include
from .views import index_product_view, product_detail_view, \
    manufacturer_detail_view, manufacturer_active_list_view

app_name = 'products'

urlpatterns = [
    path('products/', index_product_view),
    path('products/<int:pk>', product_detail_view),
    path('manufacturers/<int:pk>', manufacturer_detail_view),
    path('manufacturers/active/<str:bool>', manufacturer_active_list_view)
]
