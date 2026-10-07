from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
		"delivery_tracking",
		bootstrap_servers=["localhost:9096", "localhost:9098"],
		group_id = "tracking_group",
		auto_offset_reset="earliest",
		value_deserializer=lambda x:
		json.loads(x.decode("utf-8"))
)
for message in consumer:
	data=message.value

	print("\n---------Live Delivery----------")
	print("Delivery ID: ", data["delivery_id"])
	print("Distance: ", data["distance"], "km")
	print("Traffic: ", data["traffic"])
	print("Weather: ", data["weather"])
	print("Delivery Time: ",data["delivery_time"])
	print("Speed:", data["vehicle_speed"], "km/h")

