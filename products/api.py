import uvicorn
import json
from fastapi import FastAPI
from bson import json_util,ObjectId
from schema import  ProductCreate,ProductUpdate
from db import db

app = FastAPI()
product_collection = db.get_collection("products")

@app.get("/check")
def order_index():
    return "Product working"

@app.post("/create")
async def create_product(data:ProductCreate):
    result = product_collection.insert_one(data.__dict__)
    return {"msg":f"Product added with id {result.inserted_id}"}

@app.post("/update")
async def update_product(data:ProductUpdate):
    result = product_collection.update_one({"_id":ObjectId(data.id)},{"$set":data.__dict__})
    return {"msg":f"Product updated with id {result.upserted_id}"}

@app.delete("/delete")
async def delete_product(product_id:str):
    result = product_collection.delete_one({'_id':ObjectId(product_id)})
    return {"msg":f"Product deleted with id {result}"}

@app.get("/list")
def list_product():
    docs = [json.loads(json_util.dumps(doc)) for doc in product_collection.find()]
    return {"msg":"Products fetched successfully","data":docs}


if __name__ == "__main__":
    uvicorn.run("api:app",port=3000,reload=True)
