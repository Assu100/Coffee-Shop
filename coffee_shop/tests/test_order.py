import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_order_validation():
    customer = Customer(name="Alice")
    coffee = Coffee(name="Mocha")
    with pytest.raises(ValueError):
        Order(customer, coffee, 0.5)
    with pytest.raises(ValueError):
        Order(customer, coffee, 15.0)
