class Order:
    all_orders = []
    
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all_orders.append(self)
    
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, value):
        if hasattr(self, '_customer'):
            raise AttributeError("Cannot change order customer after initialization")
        from customer import Customer
        if not isinstance(value, Customer):
            raise ValueError("Must be a Customer instance")
        self._customer = value
    
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, value):
        if hasattr(self, '_coffee'):
            raise AttributeError("Cannot change order coffee after initialization")
        from coffee import Coffee
        if not isinstance(value, Coffee):
            raise ValueError("Must be a Coffee instance")
        self._coffee = value
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if hasattr(self, '_price'):
            raise AttributeError("Cannot change order price after initialization")
        if not isinstance(value, (int, float)) or not (1.0 <= value <= 10.0):
            raise ValueError("Price must be 1.0-10.0")
        self._price = value