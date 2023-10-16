number_of_students = int(input())

student_dict = {}

for num in range(number_of_students):
    student, grade = input().split()
    if student not in student_dict:
        student_dict[student] = []
    student_dict[student].append(float(grade))

for student, grades in student_dict.items():
    average_grade = sum(student_dict[student]) / len(student_dict[student])
    grades_list = [str(f"{grade:.2f}") for grade in grades]
    print(f'{student} -> {" ".join(grades_list)} (avg: {average_grade:.2f})')
