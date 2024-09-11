import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_name_validation():
    with pytest.raises(ValueError):
        Customer(name="")

def test_customer_create_order():
    customer = Customer(name="John")
    coffee = Coffee(name="Latte")
    order = customer.create_order(coffee, 5.0)
    assert len(customer.orders()) == 1
    assert customer.orders()[0] == order
    assert coffee.orders()[0] == order
