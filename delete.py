from main import Customer, Product, session

customer = session.query (Customer). filter (Customer.id == 1). first ()

product = session.query (Product). filter (Product.id == 1). first ()

customer.products.remove (product)

session.commit ()