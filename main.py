from fastapi import FastAPI,Depends
from models import Products
from database import session,engine
import database_model
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"]
    )

database_model.Base.metadata.create_all(bind = engine)

@app.get("/")
def greetings():
    return "hello Srushti!"

products = [
    Products(id = 1,name = "redmi12",description = "phone",price = 2000,quantity=12),
    Products(id=2,name  = "redmi11",description = "phone1",price = 20001,quantity=122)
]

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()   

def init__db():
    db = session()
    count = db.query(database_model.Product).count()
    
    if count == 0:
        for product in products:
            db.add(database_model.Product(**product.model_dump()))
        db.commit()
    
init__db()

@app.get("/products")
def get_all_products(db:Session = Depends(get_db)):
    db_products = db.query(database_model.Product).all()
    return db_products

@app.get("/products/{id}")
def get_product_by_id(id:int,db:Session = Depends(get_db)):
    db_product = db.query(database_model.Product).filter(database_model.Product.id == id).first()
    if db_product:
        return db_product
    return "Product not found!"

@app.post("/products")
def add_product(product:Products,db:Session = Depends(get_db)):
    db.add(database_model.Product(**product.model_dump()))
    db.commit()
    return product

@app.put("/products/{id}")
def update_product(id:int,product : Products,db:Session = Depends(get_db)):
    db_product = db.query(database_model.Product).filter(database_model.Product.id == id).first()
    if db_product:
        db.query(database_model.Product).filter(database_model.Product.id == id).update(product.model_dump())
        db.commit()
        return "Product updated successfully!"
    return "Product not found!"    

@app.delete("/products/{id}")
def delete_product(id:int,db:Session = Depends(get_db)):
    db_product = db.query(database_model.Product).filter(database_model.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "Product deleted successfully!"
        
    return "product not found"    
            


    