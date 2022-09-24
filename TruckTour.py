def truckTour(petrolpumps):
    # Write your code here
    fuel = 0
    position = 0
    for pump in petrolpumps:
        fuel += pump[0] - pump[1]
        if fuel < 0:
            position = petrolpumps.index(pump) + 1
            fuel = 0
    return position
