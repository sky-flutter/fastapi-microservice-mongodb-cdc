from pymongo import MongoClient


uri = "mongodb+srv://%s:%s@%s" % ("<username>", "<password>", "<db-host>")

try:
    client = MongoClient(uri)
    db = client.orders
    ecommerce = client.ecommerce
except Exception as e:
    print("Error::",e)




