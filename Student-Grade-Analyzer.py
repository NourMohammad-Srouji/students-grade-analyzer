def display_student_summary(number_of_students):
    total_grade = 0
    passed_students = 0
    names = []
    grades = []

    for num in range(number_of_students):
        student_name = input('Enter the name of the student: ')
        grade = int(input('Enter the grade of the student: '))

