from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
    DateTime,
    Float,
    Boolean,
    Date,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from uuid import UUID

from database import Base


class Supplier(Base):
    __tablename__ = "suppliers"

    suuid = Column(UUID(as_uuid=True), primary_key=True, index=True, nullable=False)
    company_name = Column(String(length=255), unique=True, nullable=False)
    contact_name = Column(String(length=255), index=True, nullable=False)
    contact_title = Column(String(length=255), nullable=False, index=True)
    address = Column(String(length=255), index=True, nullable=False)
    city = Column(String(length=255), index=True, nullable=False)
    region = Column(String(length=255), index=False, nullable=False)

    # Establishing the One-to-Many relationship
    products = relationship("Product", back_populates="supplier")

    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())


class Product(Base):
    __tablename__ = "products"

    puid = Column(UUID(as_uuid=True), primary_key=True, index=True, nullable=False)
    product_name = Column(String(length=255), index=True, nullable=False, unique=True)
    quantity_per_unit = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)
    units_in_stock = Column(Integer, nullable=False, default=0)
    units_on_order = Column(Integer, nullable=False, default=0)
    reorder_level = Column(Integer, nullable=False, default=0)
    product_status = Column(Boolean, nullable=False, default=False)

    # Relationships

    # Defining the foreign key relationship
    supplier_id = Column(Integer, ForeignKey("suppliers.id"))

    # Establishing the back-reference to the Supplier
    supplier = relationship("Supplier", back_populates="products")

    # Defining the foreign key relationship
    category_id = Column(Integer, ForeignKey("categories.id"))

    # Establishing the back-reference to the Category
    category = relationship("Category", back_populates="products")

    order_details = relationship("OrderDetail", back_populates="product")

    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())


class Category(Base):
    __tablename__ = "categories"

    cuuid = Column(UUID(as_uuid=True), primary_key=True, index=True, nullable=False)
    category_name = Column(String(length=255), nullable=False, index=True)
    description = Column(String(length=500), nullable=False)
    picture = Column(String(length=255), nullable=True)

    # Relationships
    products = relationship("Product", back_populates="category")

    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())


class OrderDetails(Base):
    __tablename__ = "order_details"

    ruid = Column(UUID(as_uuid=True), primary_key=True, index=True, nullable=False)
    unit_price = Column(Float, nullable=False)
    quantity = Column(Integer, unique=True)
    status = Column(Boolean, nullable=False, default=False)

    # Defining the foreign key relationship
    product_id = Column(Integer, ForeignKey("products.id"))

    # Establishing the back-reference to the Product
    product = relationship("Product", back_populates="order_details")

    # Defining the foreign key relationship
    order_id = Column(Integer, ForeignKey("orders.id"))

    # Establishing the back-reference to the Order
    order = relationship("Order", back_populates="order_details")

    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())


class Oders(Base):
    __tablename__ = "orders"

    oid = Column(UUID(as_uuid=True), primary_key=True, index=True, nullable=False)
    order_date = Column(DateTime, nullable=False)
    required_date = Column(DateTime, nullable=False)
    shipped_date = Column(DateTime, nullable=False)
    shipped_via = Column(String(length=255), nullable=False)
    freight = Column(String(length=255), nullable=False, index=True)
    ship_name = Column(String(length=255), nullable=False, index=False)
    ship_address = Column(String(length=255), nullable=False)
    ship_city = Column(String(length=255), nullable=False)
    ship_region = Column(String(length=255), nullable=False)
    ship_postal_code = Column(String(length=255), nullable=False)
    ship_country = Column(String(length=255), nullable=False)

    order_details = relationship("OrderDetail", back_populates="order")

    # Relationship between orders and employees
    employee_id = Column(Integer, ForeignKey("employees.id"))
    employee = relationship("Employee", back_populates="orders")

    # Defining the foreign key relationship
    employee_id = Column(Integer, ForeignKey("employees.id"))

    # Establishing the back-reference to the Employee
    employee = relationship("Employee", back_populates="orders")

    # Defining the foreign key relationship
    customer_id = Column(Integer, ForeignKey("customers.id"))

    # Establishing the back-reference to the Customer
    customer = relationship("Customer", back_populates="orders")

    # Defining the foreign key relationship
    shipper_id = Column(Integer, ForeignKey("shippers.id"))

    # Establishing the back-reference to the Shipper
    shipper = relationship("Shipper", back_populates="orders")

    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())


class Employee(Base):
    __tablename__ = "employees"

    euid = Column(UUID(as_uuid=True), primary_key=True, index=True, nullable=False)
    title = Column(String(length=25), nullable=False)
    title_of_courtesy = Column(String(length=25), nullable=False)
    first_name = Column(String(length=255), nullable=False, index=True)
    last_name = Column(String(length=255), nullable=False, index=True)
    date_of_birth = Column(Date, nullable=False)
    hire_date = Column(DateTime, nullable=False)
    address = Column(String(length=255), nullable=False)
    city = Column(String(length=255), nullable=False)
    region = Column(String(length=255), nullable=False)

    # Relationship between employees and orders
    orders = relationship("Order", back_populates="employees")

    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())


class Customer(Base):
    __tablename__ = "customers"

    cuid = Column(UUID(as_uuid=True), primary_key=True, index=True, nullable=False)
    company_name = Column(String(length=255), nullable=False, unique=True, index=True)
    company_contact = Column(String(length=255), nullable=False)
    contact_person = Column(String(length=255), nullable=False)
    customer_address = Column(String(length=255), nullable=False)
    customer_city = Column(String(length=255), nullable=False)
    customer_region = Column(String(length=255), nullable=False)
    customer_postcode = Column(String(length=255), nullable=False)

    # Establishing the One-to-Many relationship
    orders = relationship("Order", back_populates="customer")

    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())


class Shipper(Base):
    __tablename__ = "shippers"

    shuid = Column(UUID(as_uuid=True), primary_key=True, index=True, nullable=False)
    compnay_name = Column(String(length=255), nullable=False)
    phone_number = Column(String(length=30), nullable=False)

    # Establishing the One-to-Many relationship
    orders = relationship("Order", back_populates="shipper")

    time_shipped = Column(DateTime(timezone=True), server_default=func.now())
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
