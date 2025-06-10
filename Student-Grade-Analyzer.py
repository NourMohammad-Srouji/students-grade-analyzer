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