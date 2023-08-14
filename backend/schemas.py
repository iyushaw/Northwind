from pydantic import BaseModel
from typing import str, int, Optional
from datetime import date


class CreateOder(BaseModel):
    order_date: date
    required_date: date
    shipped_date: date
    shipped_via: str
    freight: str
    ship_name: str[Optional] = None
    ship_address: str[Optional] = None
    ship_city: str[Optional] = None
    ship_region: str[Optional] = None
    ship_postal_code: str[Optional] = None
    ship_country: str[Optional] = None


class CreateShipper(BaseModel):
    compnay_name: str
    phone_number: str


class CreateEmployee(BaseModel):
    title: str
    title_of_courtesy: str[Optional] = None
    first_name: str
    last_name: str
    date_of_birth: date
    hire_date: date
    address: str
    region: str


class CreateCategory(BaseModel):
    category_name: str
    description: str
    picture: str[Optional] = None


class CreateOrderDetail(BaseModel):
    unit_price: float
    quantity: int
    status: bool[Optional] = None


class CreateCustomer(BaseModel):
    company_name: str
    company_contact: str
    contact_person: str
    customer_address: str
    customer_city: str
    customer_region: str
    customer_postcode: str[Optional] = None


class CreateProduct(BaseModel):
    product_name: str
    quantity_per_unit: int
    unit_price: float
    units_in_stock: int
    units_on_order: int
    reorder_level: int[Optional] = None
    product_status: bool[Optional] = None


class CreateSupplier(BaseModel):
    company_name: str
    contact_name: str
    contact_title: str
    address: str
    city: str
    region: str
