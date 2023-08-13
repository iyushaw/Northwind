from pydantic import BaseModel
from typing import str, int, Optional


class CreateOder(BaseModel):
    pass


class CreateShipper(BaseModel):
    pass


class CreateEmployee(BaseModel):
    pass


class CreateCategory(BaseModel):
    pass


class CreateOrderDetail(BaseModel):
    pass


class CreateCustomer(BaseModel):
    pass


class CreateProduct(BaseModel):
    pass


class CreateSupplier(BaseModel):
    pass


#  Update


class UpdateOder(BaseModel):
    pass


class UpdateShipper(BaseModel):
    pass


class UpdateEmployee(BaseModel):
    pass


class UpdateCategory(BaseModel):
    pass


class UpdateOrderDetail(BaseModel):
    pass


class UpdateCustomer(BaseModel):
    pass


class UpdateProduct(BaseModel):
    pass


class UpdateSupplier(BaseModel):
    pass
