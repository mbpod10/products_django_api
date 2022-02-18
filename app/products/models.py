from django.db import models

# Create your models here.


class Manufacturer(models.Model):
    name = models.CharField(max_length=122)
    location = models.CharField(max_length=122)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=122)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="products")
    description = models.TextField()
    photo = models.ImageField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    shipping_cost = models.DecimalField(decimal_places=2, max_digits=5)
    quantity = models.SmallIntegerField()

    def __str__(self):
        return self.name
