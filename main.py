import csv


def calculate_average(marks):
    return sum(marks) / len(marks)


def get_letter_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


students = []

with open("grades.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        name = row["Name"]

        marks = [
            int(row["Assignment1"]),
            int(row["Assignment2"]),
            int(row["Midterm"]),
            int(row["Final"])
        ]

        average = calculate_average(marks)
        letter_grade = get_letter_grade(average)

        students.append({
            "name": name,
            "average": average,
            "letter_grade": letter_grade
        })


print("Student Grade Report")
print("--------------------")

for student in students:
    print(f"{student['name']}: {student['average']:.2f}% - {student['letter_grade']}")


class_average = calculate_average([student["average"] for student in students])
highest_student = max(students, key=lambda student: student["average"])
lowest_student = min(students, key=lambda student: student["average"])

print("\nClass Summary")
print("-------------")
print(f"Class Average: {class_average:.2f}%")
print(f"Highest Average: {highest_student['name']} with {highest_student['average']:.2f}%")
print(f"Lowest Average: {lowest_student['name']} with {lowest_student['average']:.2f}%")
