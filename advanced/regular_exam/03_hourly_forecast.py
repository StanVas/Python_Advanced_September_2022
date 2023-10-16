def forecast(*data):
    forecast_dict = {"Sunny": [], "Cloudy": [], "Rainy": []}

    for element in data:
        city = element[0]
        weather = element[1]
        forecast_dict[weather].append(city)

    delete = []
    for key, value in forecast_dict.items():
        if len(value) == 0:
            delete.append(key)

    for el in delete:
        del forecast_dict[el]

    output = []

    for key, value in forecast_dict.items():
        for city in sorted(value):
            output.append(f'{city} - {key}')

    return '\n'.join(output)


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
