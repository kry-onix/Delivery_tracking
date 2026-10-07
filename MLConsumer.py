from kafka import KafkaConsumer
import json
import joblib
import pandas as pd

model = joblib.load("delivery_model.pkl")

consumer = KafkaConsumer(
		"delivery_tracking",
		bootstrap_servers=["localhost:9096", "localhost:9098"],
		group_id = "ml_group",
		auto_offset_reset="earliest",
		value_deserializer=lambda x:
		json.loads(x.decode("utf-8"))
)

for message in consumer:
	data = message.value
	x = pd.DataFrame([{
		"distance": data["distance"],
		"traffic": data["traffic"],
		"weather": data["weather"],
		"delivery_speed": data["vehicle_speed"]
	}])
	prediction = model.predict(x)[0]
	probability = model.predict_proba(x)[0][1]
	print("\n--------ML Prediction---------")
	print("Delivery ID: ", data["delivery_id"])

	if prediction == 1:
		print("Prediction: Delayed")
	else:
		print("Prediction : On Time")

	print("Delay Probability : ", round(probability * 100, 2), "%")




