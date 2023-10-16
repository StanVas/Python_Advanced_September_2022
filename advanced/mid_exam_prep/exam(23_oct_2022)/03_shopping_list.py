def shopping_list(integer, **data):
    budget = integer

    if budget < 100:
        return "You do not have enough budget."

    products = {}

    for key, value in data.items():
        products[key] = 0
        price = value[0]
        quantity = value[1]
        products[key] += price * quantity

    result = []
    basket = 0

    for key, value in products.items():
        if basket == 5:
            break
        if budget >= value:
            basket += 1
            budget -= value
            result.append(f'You bought {key} for {value:.2f} leva.')

    return '\n'.join(result)


# print(shopping_list(100, microwave=(70, 2), skirts=(15, 4), coffee=(1.50, 10), ))

# print(shopping_list(20, jeans=(19.99, 1), ))
#
print(shopping_list(104, cola=(1.20, 2), candies=(0.25, 15), bread=(1.80, 1), pie=(10.50, 5), tomatoes=(4.20, 1),
                    milk=(2.50, 2), juice=(2, 3), eggs=(3, 1), ))
