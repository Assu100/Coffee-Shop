# debug.py
from customer import Customer
from coffee import Coffee

c1 = Customer(name="Alice")
c2 = Customer(name="Bob")
coffee1 = Coffee(name="Latte")
coffee2 = Coffee(name="Espresso")

order1 = c1.create_order(coffee1, 4.5)
order2 = c2.create_order(coffee1, 5.0)
order3 = c1.create_order(coffee2, 3.0)

print(c1.coffees())
print(coffee1.customers())
print(coffee1.average_price())
print(Customer.most_aficionado(coffee1))
