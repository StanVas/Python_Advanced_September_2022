def rectangle(length, wight ):
    def perimeter():
        rect_perimeter = length * 2 + wight * 2
        return f'Rectangle perimeter: {rect_perimeter}'

    def area():
        rect_area = length * wight
        return f'Rectangle area: {rect_area}'

    if not isinstance(length, int) or not isinstance(wight, int):
        return "Enter valid values!"

    return area() + '\n' + perimeter()


print(rectangle(2, 10))
