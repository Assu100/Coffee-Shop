class Customer:
    def __init__(self, name):
        self._name = None
        self.name = name  
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) < 1 or len(value) > 15:
            raise ValueError("Name must be a string between 1 and 15 characters.")
        self._name = value

    def orders(self):
        return self._orders

    def coffees(self):
        return list(set(order.coffee for order in self._orders))

    def create_order(self, coffee, price):
        from order import Order  
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee._orders.append(order)
        return order
    
    def most_aficionado(coffee):
        max_spent = 0
        aficionado = None
        for customer in coffee.customers():
            spent = sum(order.price for order in customer.orders() if order.coffee == coffee)
            if spent > max_spent:
                max_spent = spent
                aficionado = customer
        return aficionado


