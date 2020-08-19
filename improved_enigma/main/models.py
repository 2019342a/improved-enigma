from django.db import models


class Product(models.Model):
    class Sizes(models.TextChoices):
        XS = "extra small"
        S = "small"
        M = "medium"
        L = "large"
        XL = "extra large"

    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    size = models.CharField(choices=Sizes.choices, default=Sizes.M, max_length=20)

    def __repr__(self):
        return f"{self.id}-{self.name}"

    def __str__(self):
        return self.__repr__()


class Stock(models.Model):
    product = models.ForeignKey("main.Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __repr__(self):
        return f"{self.id}-{self.product.name}"

    def __str__(self):
        return self.__repr__()


class Customer(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField()

    def __repr__(self):
        return f"{self.full_name}-{self.email}"

    def __str__(self):
        return self.__repr__()


class Order(models.Model):
    customer = models.ForeignKey("main.Customer", on_delete=models.CASCADE)
    products = models.ManyToManyField("main.Product", related_name="orders")

    def __repr__(self):
        return f"{self.id}-{self.customer.full_name}"

    def __str__(self):
        return self.__repr__()
