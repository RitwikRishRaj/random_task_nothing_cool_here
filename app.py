import pickle
import __main__
from flask import Flask, request, jsonify

app = Flask(__name__)

class DeliveryMdl:
    def predict(self, dist, weight):
        time = 0.5 + (dist * 0.2) + (weight * 0.1)
        return time

__main__.DeliveryMdl = DeliveryMdl

with open("delivery_mdl.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    distance = data["distance"]
    weight = data["weight"]
    result = model.predict(distance, weight)
    return jsonify({"est_delivery_time_hrs": result})

if __name__ == "__main__":
    app.run(debug=True)