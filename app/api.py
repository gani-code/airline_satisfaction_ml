from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("app/satisfaction_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict_form():
    try:
        gender = int(request.form["gender"])
        age = int(request.form["age"])
        distance = float(request.form["distance"])
        wifi = int(request.form["wifi"])
        time_convenient = int(request.form["time_convenient"])

        features = np.array([[gender, age, distance, wifi, time_convenient]])
        prediction = model.predict(features)

        result = "Satisfied" if prediction[0] == 1 else "Dissatisfied"
        return render_template("index.html", prediction=result)

    except Exception as e:
        return render_template("index.html", prediction=f"Error: {str(e)}")

@app.route("/api/predict", methods=["POST"])
def predict_api():
    data = request.json

    try:
        gender = 1 if data['Gender'].lower() == 'male' else 0
        age = int(data['Age'])
        flight_distance = int(data['Flight Distance'])
        inflight_wifi = int(data['Inflight wifi service'])
        dep_arr_time = int(data['Departure/Arrival time convenient'])

        features = np.array([[gender, age, flight_distance, inflight_wifi, dep_arr_time]])
        prediction = model.predict(features)[0]
        result = "Satisfied" if prediction == 1 else "Dissatisfied"

        return jsonify({"prediction": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
