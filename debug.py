from customer import Customer
from coffee import Coffee
from order import Order

# Test your code
customer1 = Customer("Alice")
customer2 = Customer("Bob")

coffee1 = Coffee("Espresso")
coffee2 = Coffee("Latte")

order1 = customer1.create_order(coffee1, 5.0)
order2 = customer1.create_order(coffee2, 7.5)
order3 = customer2.create_order(coffee1, 3.0)

print("Customer 1 orders:", customer1.orders())
print("Customer 1 coffees:", customer1.coffees())
print("Coffee 1 customers:", coffee1.customers())
print("Coffee 1 num orders:", coffee1.num_orders())
print("Coffee 1 average price:", coffee1.average_price())
print("Most aficionado for coffee1:", Customer.most_aficionado(coffee1))