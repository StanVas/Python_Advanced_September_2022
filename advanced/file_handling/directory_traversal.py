import os


def extract_files(directory):
    return [el for el in directory if '.' in el]


def get_report(files):
    files_dict = {}
    for file in files:
        filename, extension = file.split('.')
        if extension not in files_dict:
            files_dict[extension] = []
        files_dict[extension].append(file)
    return files_dict


directory = input()
directory = os.listdir(directory)

files = extract_files(directory)
report = get_report(files)

result = []
extensions = sorted(report.items(), key=lambda x: x[0])

for extension, files in extensions:
    result.append(f'.{extension}\n')
    for file in sorted(files):
        result.append(f'- - - {file}\n')

with open('report.txt', 'w') as file:
    file.write("".join(result))
