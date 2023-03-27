from main import Customer, Product, session

# customer = Customer(name = 'customer 1')
# customer2 = Customer(name = 'customer 2')
# customer3 = Customer(name = 'customer 3')

customer = session.query(Customer).filter(Customer.id == 1).first()
customer2 = session.query(Customer).filter(Customer.id == 2).first()

product4 = Product(name = "Chips", price = 4)
product2 = Product(name = "Burger", price = 10)
product3 = Product(name = "Coke", price = 2)
product = Product(name = "Cake", price = 6)

customer2.products.append(product2)
customer2.products.append(product3)

# session.add_all([customer, customer2, customer3])
session.commit() 

print(customer.products)