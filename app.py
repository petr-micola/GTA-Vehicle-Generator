from flask import Flask, render_template, request, jsonify
from backend import fetch_vehicle_data, filter_and_generate_random_vehicle

app = Flask(__name__)

@app.route("/")
def index():
    # Load initial data from the backend
    vehicle_data = fetch_vehicle_data()
    vehicle_classes = list(vehicle_data.keys())
    return render_template(
        "index.html",
        vehicle_classes=vehicle_classes,
        lowest_price=0,
        highest_price=10000000,
    )

@app.route("/generate", methods=["POST"])
def generate_random_vehicle():
    # Get user-selected filters
    selected_classes = request.form.getlist("vehicle_class")
    min_price = int(request.form["min_price"])
    max_price = int(request.form["max_price"])

    # Load data from the backend and generate a random vehicle
    vehicle_data = fetch_vehicle_data()
    random_vehicle = filter_and_generate_random_vehicle(
        vehicle_data, selected_classes, min_price, max_price
    )

    return jsonify(random_vehicle)

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
