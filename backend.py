import requests
import random

# Define the GTA API URL
API_URL = "https://gta.now.sh/api/vehicles/all"

def fetch_vehicle_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    return []

def filter_and_generate_random_vehicle(data, selected_classes, min_price, max_price):
    filtered_vehicles = []

    for vehicle_class_name, vehicles in data.items():
        if vehicle_class_name in selected_classes:
            for vehicle_name, vehicle_details in vehicles.items():
                if (
                    "price" in vehicle_details
                    and min_price <= int(vehicle_details["price"]) <= max_price
                ):
                    filtered_vehicles.append(
                        {
                            "class": vehicle_class_name,
                            "name": vehicle_name,
                            **vehicle_details,
                            "image_url": vehicle_details.get("images", {}).get(
                                "front", ""
                            ),
                        }
                    )

    if filtered_vehicles:
        random_vehicle = random.choice(filtered_vehicles)
        return random_vehicle
    return {"error": "No matching vehicles found"}
