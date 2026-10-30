distance_km = 300.0
fuel_price_per_liter = 2.00

vehicles = [
    ("Car A", 15.0),
    ("Car B", 12.0),
    ("Car C", 20.0)
]

min_cost = float('inf')
best_vehicle = ""

print(f"Trip Distance: {distance_km} km | Fuel Price: ${fuel_price_per_liter:.2f}/L\n")

for name, mileage in vehicles:
    fuel_needed = distance_km / mileage
    trip_cost = fuel_needed * fuel_price_per_liter

    print(f"{name}: Mileage = {mileage} km/l | Fuel Needed = {fuel_needed:.1f}L | Total Cost = ${trip_cost:.2f}")

    if trip_cost < min_cost:
        min_cost = trip_cost
        best_vehicle = name

print("\n--- Route Cost Recommendation ---")
print(f"Most Economical Option: {best_vehicle} at ${min_cost:.2f}")