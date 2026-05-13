from fastapi import FastAPI, HTTPException, Query
from service.products import get_all_products
app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "welcome to fastapi app."}

#@app.get("/products")
#def get_products():
 #   return get_all_products()
 
@app.get("/products")
def list_products(name: str = Query (default=None, min_length=1,max_length=100,description="Search product by name(case insensitive)")):
    products = get_all_products()
    if name :
        needle = name.strip().lower()
        product = [p for p in products if needle in p.get("name", "").lower()]
        
        if not product:
            raise HTTPException(status_code=404, detail=f"Product not found with name: {name}")
        
        total = len(product)
    
    
    return{"total": len(product), "items": product}

