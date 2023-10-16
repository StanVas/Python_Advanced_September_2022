# https://judge.softuni.org/Contests/Practice/Index/3515#2
def shopping_cart(*data):
    shopping_dict = {'Pizza': [], 'Soup': [], 'Dessert': []}

    for element in data:
        if element == 'Stop':
            break

        type_of_meal = element[0]
        product = element[1]

        if type_of_meal == 'Soup':
            if len(shopping_dict[type_of_meal]) == 3:
                continue
        elif type_of_meal == 'Pizza':
            if len(shopping_dict[type_of_meal]) == 4:
                continue
        elif type_of_meal == 'Dessert':
            if len(shopping_dict[type_of_meal]) == 2:
                continue
        if product not in shopping_dict[type_of_meal]:
            shopping_dict[type_of_meal].append(product)

    for value in shopping_dict.values():
        if len(value) > 0:
            break
    else:
        return 'No products in the cart!'

    result = ''
    shopping_dict = sorted(shopping_dict.items(), key=lambda x: (-len(x[1]), x[0]))

    for el in shopping_dict:
        result += f'{el[0]}:\n'
        sorted_products = sorted(el[1])
        for product in sorted_products:
            result += f'- {product}\n'

    return result


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'ham'),
#     'Stop',
# ))
#
# print(shopping_cart(
#     'Stop',
#     ('Pizza', 'ham'),
#     ('Pizza', 'mushrooms'),
# ))
