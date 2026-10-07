import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = pd.read_csv("delivery_data.csv")

X = data[["distance","traffic","weather","delivery_speed",]]
Y = data["delayed"]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=42, test_size=0.2)

model = LogisticRegression()
model.fit(X_train, Y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(Y_test, y_pred)
print("Model Accuracy: ", accuracy)

joblib.dump(model, "delivery_model.pkl")
print("model saved Successfully")
