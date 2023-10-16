# https://judge.softuni.org/Contests/Practice/Index/3374#2
def start_spring(**data):
    spring_objects = {}
    result = []

    for value, key in data.items():
        if key not in spring_objects:
            spring_objects[key] = []

        spring_objects[key].append(value)

    spring_objects = sorted(spring_objects.items(), key=lambda x: (-len(x[1]), x[0]))
    for key, values in spring_objects:
        result.append(f'{key}:')

        for value in sorted(values):
            result.append(f'-{value}')

    return '\n'.join(result)


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower", }
print(start_spring(**example_objects))
