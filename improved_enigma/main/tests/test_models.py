import pytest

from .factories import CustomerFactory
from .factories import OrderFactory
from .factories import ProductFactory
from .factories import StockFactory

pytestmark = pytest.mark.django_db


def test_customer_str():
    customer = CustomerFactory()
    assert repr(customer) == f"{customer.full_name}-{customer.email}"
    assert str(customer) == f"{customer.full_name}-{customer.email}"


def test_order_str():
    order = OrderFactory()
    assert repr(order) == f"{order.id}-{order.customer.full_name}"
    assert str(order) == f"{order.id}-{order.customer.full_name}"


def test_product_str():
    product = ProductFactory()
    assert repr(product) == f"{product.id}-{product.name}"
    assert str(product) == f"{product.id}-{product.name}"


def test_stock_str():
    stock = StockFactory()
    assert repr(stock) == f"{stock.id}-{stock.product.name}"
    assert str(stock) == f"{stock.id}-{stock.product.name}"
