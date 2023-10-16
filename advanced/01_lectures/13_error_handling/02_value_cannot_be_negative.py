class ValueCannotBeNegative(Exception):
    """Number is below zero"""
    pass


# in this case we rise our exception as error
for i in range(5):
    number = int(input())
    if number < 0:
        raise ValueCannotBeNegative

# in this one we get text from the exception and our while loop continues
while True:
    try:
        x = int(input('Please enter a number: '))
        break
    except ValueError:
        print('Oops! That was not valid number. Try again...')
