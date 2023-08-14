from fastapi import FastAPI

categories = ["customers", "orders", "products", "employees"]

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Welcome to Northwind API"}


# Customers Routes
@app.get("/customers")
def get_customers():
    return {"message": "All Customers"}


@app.get("/customer/{id}")
def get_one_customer(id: int):
    return {"Customer": f"Customer with {id}"}


@app.post("/customer/")
def add_customer():
    return {"Customer": "New Customer Created."}


# Orders Routes
@app.get("/orders")
def get_orders():
    return {"message": "All Orders"}


@app.get("/order/{id}")
def get_one_order(id: int):
    return {"Order": f"Order with {id}"}


@app.post("/order/")
def add_order():
    return {"Order": "New Order Created."}


# Products Routes
@app.get("/products")
def get_products():
    return {"message": "All Products"}


@app.get("/product/{id}")
def get_one_product(id: int):
    return {"Product": f"Product with {id}"}


@app.post("/product/")
def add_product():
    return {"Product": "New Product Created."}


# Employees Routes
@app.get("/employees")
def get_customers():
    return {"message": "All Employees"}


@app.get("/employee/{id}")
def get_one_employee(id: int):
    return {"Employee": f"Employee with {id}"}


@app.post("/employee/")
def add_employee():
    return {"Customer": "New Employee Created."}
