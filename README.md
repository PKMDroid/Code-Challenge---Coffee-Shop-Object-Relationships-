# Code-Challenge---Coffee-Shop-Object-Relationships-
# Coffee Shop Domain Model

## Description
A Python application that models a Coffee Shop domain using Object-Oriented Programming (OOP) principles. This project demonstrates class design, object relationships, data validation, and the implementation of a many-to-many relationship between Customers and Coffees through Orders.

## Project Structure
```
coffee_shop/
│
├── customer.py          # Customer class implementation
├── coffee.py            # Coffee class implementation
├── order.py             # Order class implementation
└── README.md            # Project documentation
```

## Domain Model

### Relationships
- A **Customer** can place many **Orders**
- A **Coffee** can have many **Orders**
- An **Order** belongs to one **Customer** and one **Coffee**
- **Customer** and **Coffee** have a **many-to-many** relationship through **Order**

## Class Descriptions

### Customer Class (`customer.py`)

**Attributes:**
- `name` (str): Customer name, must be 1-15 characters

**Methods:**
- `orders()`: Returns a list of all Order instances for the customer
- `coffees()`: Returns a unique list of Coffee instances the customer has ordered
- `create_order(coffee, price)`: Creates a new Order for the customer
- `most_aficionado(coffee)` (class method): Returns the Customer who has spent the most on a given coffee

### Coffee Class (`coffee.py`)

**Attributes:**
- `name` (str): Coffee name, must be at least 3 characters

**Methods:**
- `orders()`: Returns a list of all Order instances for this coffee
- `customers()`: Returns a unique list of Customer instances who ordered this coffee
- `num_orders()`: Returns the total number of times this coffee has been ordered
- `average_price()`: Returns the average price of all orders for this coffee

### Order Class (`order.py`)

**Attributes:**
- `customer` (Customer): The customer who placed the order
- `coffee` (Coffee): The coffee that was ordered
- `price` (float): The price of the order, must be between 1.0 and 10.0

**Note:** All attributes are immutable after initialization and include validation.

## Usage Examples

```python
from customer import Customer
from coffee import Coffee

# Create customers
alice = Customer("Alice")
bob = Customer("Bob")

# Create coffees
espresso = Coffee("Espresso")
latte = Coffee("Latte")

# Place orders
order1 = alice.create_order(espresso, 5.00)
order2 = alice.create_order(latte, 7.50)
order3 = bob.create_order(espresso, 4.00)

# Query relationships
print(alice.coffees())           # [Espresso, Latte]
print(espresso.customers())      # [Alice, Bob]
print(espresso.num_orders())     # 2
print(espresso.average_price())  # 4.50

# Find top customer
top_customer = Customer.most_aficionado(espresso)
print(top_customer.name)  # "Alice"
```

## Validation Rules
- **Customer name**: String, 1-15 characters
- **Coffee name**: String, minimum 3 characters
- **Order price**: Float/Integer, between 1.0 and 10.0
- **Order customer**: Must be a Customer instance
- **Order coffee**: Must be a Coffee instance

All properties raise appropriate exceptions for invalid inputs and cannot be modified after initialization.

---

Created as part of a Python OOP assessment.