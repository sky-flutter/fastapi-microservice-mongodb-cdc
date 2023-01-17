# fastapi-microservice-mongodb-cdc
Implementation of microservices in fastapi with mongodb, CDC and KAFKA

### Create virtualenv using
python3 -m venv myenv or virtualenv myenv

### Install necessary packages for linux
source myenv/bin/activate && pip install -r requirements.txt

<p>Setup db connection username, password and db host in db.py</p>

### Setup KAFKA broker and run on 9092 port
### Create KAFKA topic using CLI command
kafka-topic --bootstrap-server localhost:9092 --create --topic dashboardtopic

Now run the project.

1. python products/api.py
2. python orders/api.py
3. python kafka_mongo/kafka_consumer.py
4. python kafka_mongo/order_change_stream.py
5. python kafka_mongo/product_change_stream.py


All set, now hit the API on URL 3000 and 3001 by http://localhost:3000 or http://localhost:3001.



