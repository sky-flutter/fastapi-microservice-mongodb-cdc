import json
from db import client
from kafka import KafkaConsumer
from bson.objectid import ObjectId

consumer = KafkaConsumer("dashboardtopic",bootstrap_servers="localhost:9092",value_deserializer=lambda m: json.loads(m))

def consume_msg(data):
    msg = json.loads(data)
    print(msg)
    if msg['operationType'] == "insert":
        collection,payload = get_insert_payload(msg)
        inserted_id = client.ecommerce[collection].insert_one(payload)
        print("Inserted ID :: ",inserted_id)
    elif msg['operationType'] == "update":
        collection,doc_id,payload = get_update_payload(msg)
        updated_id = client.ecommerce[collection].update_one({"_id":ObjectId(doc_id)},{"$set":payload})
        print("Updated ID :: ",updated_id)
    elif msg['operationType'] == "delete":
        collection = msg['ns']['coll']
        doc_id = msg['documentKey']['_id']['$oid']
        result = client.ecommerce[collection].delete_one({'_id':ObjectId(doc_id)})
        print("Deleted item result: ",result)
    else:
        pass
    
def get_update_payload(msg):
    payload = msg['updateDescription']['updatedFields']
    collection = msg['ns']['coll']
    doc_id = msg['documentKey']['_id']['$oid']
    return (collection,doc_id,payload)

def get_insert_payload(msg):
    msg['fullDocument'].pop("_id")
    doc_id = msg['documentKey']['_id']['$oid']
    payload = msg['fullDocument']
    payload['_id'] = ObjectId(doc_id)
    collection = msg['ns']['coll']
    return (collection,payload)


while True:
    for message in consumer:
        print(message.value)
        consume_msg(message.value)