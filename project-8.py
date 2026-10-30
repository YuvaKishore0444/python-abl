bus_capacity = 50
stops_data = [(20, 0), (15, 5), (30, 10)]

current_passengers = 0

print(f"Bus Operating Capacity: {bus_capacity} seats\n")

for stop_num, (boarded, alighted) in enumerate(stops_data, start=1):
    current_passengers += (boarded - alighted)

    if current_passengers > bus_capacity:
        status = "ALERT: OVER CAPACITY"
    else:
        status = "STATUS: OK"

    print(f"Stop {stop_num}: +{boarded} boarded, -{alighted} alighted | Total Onboard: {current_passengers} | {status}")