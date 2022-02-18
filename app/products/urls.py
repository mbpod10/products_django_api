from django.urls import path, include
from .views import index_product_view, product_detail_view

app_name = 'products'

urlpatterns = [
    path('products/', index_product_view),
    path('products/<pk>', product_detail_view)
]
