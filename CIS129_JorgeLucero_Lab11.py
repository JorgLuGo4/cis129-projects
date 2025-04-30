#Script: CIS129_JorgeLucero_Lab11
#Action: This code follows the instructions under 9.1, 9.2, and 9.3 exercises in Deitel & Deitel
#Author: Jorge Lucero
#Date: 4/30/25

# 9.1 exercise begins here:
with open('grades.txt', mode='w') as grades_file:
    while True:
        grade_input = input("Enter a grade (or type 'done' to finish): ")
        
        if grade_input.lower() == 'done':
            break
        
        try:
            grade = float(grade_input)
            grades_file.write(f'{grade}\n')
        except ValueError:
            print("not a valid number. Please enter a grade or 'done'.")

# 9.2 exercise begins here: (9.1 and 9.2 can both run together or independently)
with open('grades.txt', 'r') as file:
    total = 0
    count = 0

    print("Grades:")

    for line in file:
        grade = float(line)
        print(grade)
        total += grade
        count += 1

if count > 0:
    average = total / count
    print("Total:", total)
    print("Number of grades:", count)
    print("Average:", round(average, 2))
else:
    print("No grades found.")




# 9.3 exercise begins here: (This one is unrelated to 9.1 and 9.2)
import csv 

with open('grades.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

    while True:
        first_name = input("Enter student's first name (or type 'done' to stop): ")

        if first_name.lower() == 'done':
            break

        last_name = input("Enter student's last name: ")

        try:
            exam1 = int(input("Enter grade for Exam 1: "))
            exam2 = int(input("Enter grade for Exam 2: "))
            exam3 = int(input("Enter grade for Exam 3: "))
        except ValueError:
            print("Please enter valid numbers for the grades.")
            continue

        writer.writerow([first_name, last_name, exam1, exam2, exam3])

    print("Data has been saved to grades.csv")

