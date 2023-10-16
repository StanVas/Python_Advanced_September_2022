def flights(*data):
    flights_dict = {}
    for element in range(0, len(data), 2):
        if data[element] == 'Finish':
            break
        city = data[element]
        passengers = data[element + 1]
        if city not in flights_dict:
            flights_dict[city] = 0
        flights_dict[city] += passengers

    return flights_dict




print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))

print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))

print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))