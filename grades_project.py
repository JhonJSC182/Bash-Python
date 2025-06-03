print('Process Student Grades \n')

student_num = int(input('Enter the number of students '))

students = {}

for i in range(student_num):
    student_name = input(f"Enter student {i + 1} name: ")
    grades = [] / 5

    for j in range(5):
        grade = int(input(f"Enter grade {j + 1} for {student_name} "))
        grades.append(grade)


    students[student_name] = grades

