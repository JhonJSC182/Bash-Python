print('Process Student Grades \n')

student_num = int(input('Enter the number of students '))

students = {}

for i in range(student_num):
    student_name = input(f"Enter student {i + 1} name: ")
    grades = []

    for j in range(5):
        grade = int(input(f"Enter grade {j + 1} for {student_name} "))
        grades.append(grade)


    students[student_name] = grades

total_average = 0


for name, grades in students.items():
    average = sum(grades) / len(grades)
    total_average += average

    print(f"{name}'s average grade is {average}")
    
    if average >= 90:
        print(f"{name}'s grade is A")
    elif average >= 80:
        print(f"{name}'s grade is B")
    elif average >= 70:
        print(f"{name}'s grade is C")
    elif average >= 60:
        print(f"{name}'s grade is D")
    else:
        print(f"{name}'s grade is F")

    
class_average = total_average / student_num

print(f"\n The average class grade is {class_average}")