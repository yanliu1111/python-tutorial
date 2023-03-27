import os

from sqlalchemy import (Column, ForeignKey, Integer, String, Table,
                        create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

connetion_str = 'sqlite:///' + os.path.join(BASE_DIR, 'site_MtoM.sqlite3')

engine = create_engine(connetion_str, echo=True)

Base =  declarative_base()

"""
table association:
    product_id: int fk(Product.id)
    customer_id: int fk(Customers.id)

class Customer:
    id: int pk
    name: str

class Product:
    id: int pk
    name: str
    price: int
"""

association_table = Table('association', Base.metadata, Column('customer_id',ForeignKey('customers.id')),
Column('product_id',ForeignKey('products.id')))

class Customer(Base):
    __tablename__ ='custormers'
    id = Column(Integer(), primary_key=True)
    name = Column (String(40), nullable=False)
    products = relationship('Product', secondary=association_table, back_populates='customers')
    def __repr__(self):
        return f"<Custmer {self.name}>"
    
class Product(Base):
    __tablename__='products'
    id = Column (Integer(), primary_key=True)
    name = Column (String(40), nullable=False)
    price = Column (Integer(), nullable=False)
    customers = relationship('Customer', secondary=association_table, back_populates='products')
    def __repr__(self):
        return f"<Product {self.name}>"

Base.metadata.create_all(engine)