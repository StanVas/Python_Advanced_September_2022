from pyfiglet import figlet_format


def print_art(message):
    ascii_art = figlet_format(msg, font='banner3-D')  # doh
    print(ascii_art)


msg = input()
print_art(msg)
