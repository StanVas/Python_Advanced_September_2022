import re


def replace_symbols(line):
    pattern = r"[-,.!?]"
    result = re.sub(pattern, "@", line)
    return result


with open("text_even_lines.txt", "r") as file:
    lines = file.readlines()

    for line_number in range(len(lines)):

        if line_number % 2 == 0:
            replaced = replace_symbols(lines[line_number]).split()
            print(' '.join(replaced[::-1]))
