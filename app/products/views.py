from traceback import print_tb
from django.http import JsonResponse
from .models import Manufacturer, Product
from django.core.exceptions import ObjectDoesNotExist


def index_product_view(request):
    products = Product.objects.all()
    data = {"data": list(products.values())}
    return JsonResponse(data, safe=False)


def product_detail_view(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        print(product.manufacturer)
        response = {
            "data":
            {
                "name": product.name,
                "manufacturer": {
                    'name': product.manufacturer.name,
                    'location': product.manufacturer.location,
                    'active': product.manufacturer.active
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


def manufacturer_detail_view(request, pk):
    try:
        manufacturer = Manufacturer.objects.get(pk=pk)
        response = {
            "data": {
                "name": manufacturer.name,
                "location": manufacturer.location,
                "active": manufacturer.active,
                "products": []
            }
        }
        # products = list(Product.objects.filter(manufacturer=manufacturer))
        products = list(manufacturer.products.all())
        for product in products:
            response["data"]["products"].append(
                {
                    "name": product.name,
                    "description": product.description,
                    "photo": product.photo.url,
                    "price": product.price,
                    "shipping_cost": product.shipping_cost,
                    "quantity": product.quantity
                }
            )

    except ObjectDoesNotExist:
        response = {"status": 401}

    return JsonResponse(response)


def manufacturer_active_list_view(request, bool):
    if bool == "true":
        req = True
    elif bool == "false":
        req = False
    manufactures = list(Manufacturer.objects.filter(active=req))
    data = {
        f"{bool}": []
    }
    for manufacturer in manufactures:
        data[f"{bool}"].append({
            "name": manufacturer.name,
            "location": manufacturer.location,
            "active": manufacturer.active,
        })

    return JsonResponse(data)
