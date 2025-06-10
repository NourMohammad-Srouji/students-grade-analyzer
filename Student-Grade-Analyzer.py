def display_student_summary(number_of_students):
    total_grade = 0
    passed_students = 0
    names = []
    grades = []

    for num in range(number_of_students):
        student_name = input('Enter the name of the student: ')
        grade = int(input('Enter the grade of the student: '))
        # testing the validation of the grade entered
        while grade < 0 or grade > 100 :
            print(grade, 'is invalid grade')
            grade = int(input('Please enter a new valid grade: '))
        
        if grade >= 60:
            passed_students += 1

        names.append(student_name)
        grades.append(grade)

        total_grade += grade

    print("Students' Summary")
    print('--------------------')

    for i in range(len(names)):
            print('Student', i+1)
            print('Your name is', names[i])
            print('Your grade is', grades[i])
    print()

    get_avg_grade(number_of_students, total_grade)
    get_highest_grade(names, grades)
    count_passed(passed_students)

def get_avg_grade(number_of_students, total_grade):
    average_grade = total_grade / number_of_students
    print('The average grade is', average_grade)

def get_highest_grade(names, grades):
    maximum = 0
    for i in grades:
        if i > maximum:
            maximum = i
            
    for i in range(len(grades)):
        if grades[i] == maximum:
            print(names[i], 'is the student with the highest grade')
            print(grades[i], 'is the grade of', names[i])

def count_passed(passed_students):
    print('The number of passed students is', passed_students)
        
number_of_students = int(input('Enter the number of students: '))

while number_of_students <= 0:
    print(number_of_students, 'is invalid number of students')
    number_of_students = int(input('Please enter a new valid number of students: '))




