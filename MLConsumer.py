from kafka import KafkaConsumer, KafkaProducer
import json
import joblib
import pandas as pd

B = ["localhost:9096", "localhost:9098"]
model = joblib.load("delivery_model.pkl")

consumer = KafkaConsumer(
		"delivery_tracking",
		bootstrap_servers=B,
		group_id = "ml_group",
		auto_offset_reset="earliest",
		value_deserializer=lambda x:
		json.loads(x.decode("utf-8"))
)
out = KafkaProducer(
	bootstrap_servers=B,
	value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

for message in consumer:
	data = message.value
	x = pd.DataFrame([{
		"distance": data["distance"],
		"traffic": data["traffic"],
		"weather": data["weather"],
		"delivery_speed": data["vehicle_speed"]
	}])
	prediction = int(model.predict(x)[0])
	probability = float(model.predict_proba(x)[0][1])
	print("\n--------ML Prediction---------")
	print("Delivery ID: ", data["delivery_id"])
	print("Prediction: Delayed" if prediction == 1 else  "On Time")
	print("Delay Probability : ", round(probability * 100, 2), "%")
	out.send("delay-predictions", {
		"delivery_id": data["delivery_id"],
		"delayed": prediction,
		"delayed_probability": round(probability, 4),
	})
	out.flush()



