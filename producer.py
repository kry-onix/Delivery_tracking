from kafka import KafkaProducer
import json
import random
import time

producer = KafkaProducer(
	bootstrap_servers=["localhost:9096", "localhost:9098"],
		value_serializer=lambda x:
	json.dumps(x).encode("utf-8")
)

while True:
	delivery = {
		"delivery_id": "D" + str(random.randint(100, 999)),
		"distance": round(random.uniform(1,15), 2),
		"traffic": random.randint(1, 3),
		"weather": random.randint(0, 2),
		"delivery_time": random.randint(10, 50),
		"vehicle_speed": random.randint(10, 40),
	}
	producer.send(
		"delivery_tracking",
		value=delivery
	)
	print("Sent: ",delivery)
	time.sleep(3)

