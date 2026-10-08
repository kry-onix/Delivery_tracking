# Delivery Delay Prediction

Real-time pipeline: Kafka + scitkit-learn.

Flow: producer.py -> delivery_tracking topic -> MLConsumer.py -> delay-predictions topic

Stack: Kafka 4.3.1 (2 brokers), Python, scikit-learn

Run: pip install -r requirements.txt, pyhton3 model.py, pyhton3 MLConsumer.py, python3 producer.py

Model: Logistic Regression, accuracy 0.85
Confusion matrix: [[161 34] [26 179]]
