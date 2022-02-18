from django.http import JsonResponse
from .models import Product
from django.core.exceptions import ObjectDoesNotExist


def index_product_view(request):
    products = Product.objects.all()
    data = {"data": list(products.values())}
    return JsonResponse(data, safe=False)


def product_detail_view(request, pk):
    # print()
    try:
        product = Product.objects.get(pk=pk)
        response = {
            "data":
            {
                "name": product.name,
                "manufacturer": {
                    'name': product.manufacturer.name,
                    'location': product.manufacturer.location
                },
                "description": product.description,
                "photo": product.photo.url,
                "price": product.price,
                "shipping_cost": product.shipping_cost,
                "quantity": product.quantity

            }
        }
    except ObjectDoesNotExist:
        response = {"status": 401}

    return JsonResponse(response)
