from db import client
from bson.json_util import dumps
from kafka_producer import send_message
# from change_stream import ChangeStream

print("Listening Products Collection started...")
with client.products.watch() as stream:
    for change in stream:
        data = dumps(change)
        print(data)
        send_message(data)
        print('') 

# class ProductChangeStream(ChangeStream):
#     def __init__(self) -> None:
#         super().__init__(client.products)