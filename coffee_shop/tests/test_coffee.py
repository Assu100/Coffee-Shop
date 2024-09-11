import pytest
from coffee import Coffee
from customer import Customer
from order import Order

def test_coffee_name_validation():
    with pytest.raises(ValueError):
        Coffee(name="AB")

def test_coffee_num_orders():
    coffee = Coffee(name="Espresso")
    customer = Customer(name="Jane")
    customer.create_order(coffee, 3.0)
    assert coffee.num_orders() == 1
