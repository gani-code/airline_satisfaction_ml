import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import joblib

print("Current working directory:", os.getcwd())

data_path = "data/airline_passenger_satisfaction.csv"
df = pd.read_csv(data_path)
print("Data loaded successfully!")
print("Columns in dataset:", df.columns.tolist())

le_gender = LabelEncoder()
df['Gender'] = le_gender.fit_transform(df['Gender'])  # Male=1, Female=0

le_satisfaction = LabelEncoder()
df['Satisfaction'] = le_satisfaction.fit_transform(df['Satisfaction'])  # Satisfied=1, Dissatisfied=0

X = df.drop('Satisfaction', axis=1)
y = df['Satisfaction']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

model_path = "app/satisfaction_model.pkl"
joblib.dump(model, model_path)
print(f"Model saved to {model_path}")
