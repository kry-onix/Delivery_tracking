import numpy as np
import pandas as pd

np.random.seed(42)
n = 2000

distance = np.random.uniform(1, 20, n).round(1)
traffic = np.random.randint(1,4,n)
weather = np.random.randint(0, 3, n)
delivery_speed = np.random.randint(10, 40, n)

score = (distance * 0.3 + traffic *1.2 +weather *1.0 - delivery_speed * 0.1 + np.random.normal(0, 1.5, n))
delayed = (score > np.median(score)).astype(int)

df = pd.DataFrame({
	"distance": distance,
	"traffic": traffic,
	"weather": weather,
	"delivery_speed": delivery_speed,
	"delayed": delayed
})
df.to_csv("delivery_data.csv", index=False)
print(df.shape)
print(df["delayed"].value_counts())


