from string import punctuation

output_file = open("output_line_numbers.txt", "a")

with open("text_line_numbers.txt", "r") as file:
    lines = file.readlines()

    for line_idx in range(len(lines)):
        punctuation_marks = 0
        letters = 0
        current_line = lines[line_idx]
        for element in current_line:
            if element.isalpha():
                letters += 1
            elif element in punctuation:
                punctuation_marks += 1

        output_file.write(f"Line{line_idx + 1}: {current_line[:-1]} ({letters})({punctuation_marks})\n")

output_file.close()
