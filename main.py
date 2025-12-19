from fastapi import FastAPI
from models import Products

app = FastAPI()

@app.get("/")
def greetings():
    return "hello Srushti!"

products = [
    Products(id = 1,name = "redmi12",description = "phone",price = 2000,quantity=12),
    Products(id=2,name  = "redmi11",description = "phone1",price = 20001,quantity=122)
]

@app.get("/products")
def get_all_products():
    return products

@app.get("/product/{id}")
def get_product_by_id(id:int):
    for product in products:
        if product.id == id:
            return product
    return "Product not found!"

@app.post("/product")
def add_product(product:Products):
    products.append(product)
    return product

@app.put("/product/{id}")
def update_product(id:int,product : Products):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product added successfully!"
        
    return "id not matched!"    

@app.delete("/product/{id}")
def delete_product(id:int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product deleted successfully!"
        
    return "product not found"    
            


    