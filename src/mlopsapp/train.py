from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler

import joblib


dataset = fetch_california_housing()
x = dataset.data
y = dataset.target

scaler = StandardScaler()
x = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state = 42)

svr = SVR(kernel="rbf", C=100, gamma=0.1, epsilon=0.1)
svr.fit(x_train, y_train)

predictions = svr.predict(x_test)
mae = mean_absolute_error(y_test, predictions)
print(f"Mean absolute error {mae:.2f}")

r2_score = r2_score(y_test,predictions)
print(f"R2-Score {r2_score:.2f}")

joblib.dump(svr, "model.pkl")
print("Model saved into: src/model.pkl ")