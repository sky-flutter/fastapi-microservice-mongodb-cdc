import uvicorn
import json
from fastapi import FastAPI
from schema import  OrderCreate
from db import db,ecommerce
from bson import json_util
app = FastAPI()
orders_collection = db.get_collection("orders")


@app.get("/check")
def order_index():
    return "Order working"

@app.post("/create")
def create_order(data:OrderCreate):
    result = orders_collection.insert_one(data.__dict__)
    return {"msg":f"Order placed successully with id {result.inserted_id}"}


@app.get("/list")
def list_order():
    result = ecommerce.orders.aggregate([
        {
            '$lookup': {
                'from': 'products', 
                'localField': 'slug', 
                'foreignField': 'slug', 
                'as': 'products'
            }
        }
    ])  
    docs = []
    for doc in result:
        item = json.loads(json_util.dumps(doc))
        print(item) 
        docs.append(item)
    return docs


if __name__ == "__main__":
    uvicorn.run("api:app",port=3001,reload=True)