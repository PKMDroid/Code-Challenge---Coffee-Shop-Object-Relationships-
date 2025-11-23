from order import Order

class Customer:
    all_customers = []

    def __init__(self, name):
        self.name = name
        Customer.all_customers.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            raise AttributeError("Cannot change customer name after initialization")
        if not isinstance(value, str) or not (1 <= len(value) <= 15):
            raise ValueError("Name must be 1-15 characters.")
        self._name = value

    def orders(self):
        return [order for order in Order.all_orders if order.customer == self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        orders = coffee.orders()
        if not orders:
            return None
        spend = {}
        for order in orders:
            spend[order.customer] = spend.get(order.customer, 0) + order.price
        return max(spend, key=spend.get)