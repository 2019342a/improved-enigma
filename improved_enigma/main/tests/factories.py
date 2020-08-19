from factory.django import DjangoModelFactory
from factory import Faker
from factory import SubFactory

from ..models import Customer
from ..models import Order
from ..models import Product
from ..models import Stock


class CustomerFactory(DjangoModelFactory):
    full_name = Faker("name")
    email = Faker("email")

    class Meta:
        model = Customer


class ProductFactory(DjangoModelFactory):
    name = Faker("name")
    description = Faker("text")

    class Meta:
        model = Product


class StockFactory(DjangoModelFactory):
    product = SubFactory(ProductFactory)

    class Meta:
        model = Stock


class OrderFactory(DjangoModelFactory):
    customer = SubFactory(CustomerFactory)

    class Meta:
        model = Order
