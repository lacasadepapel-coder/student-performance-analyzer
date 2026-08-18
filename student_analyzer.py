import csv

def calculate_grade(average):
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

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        marks = [
            float(row["Python"]),
            float(row["Java"]),
            float(row["SQL"]),
            float(row["C"])
        ]

        average = sum(marks) / len(marks)

        student = {
            "name": row["Name"],
            "average": average,
            "grade": calculate_grade(average)
        }

        students.append(student)


print("\nSTUDENT PERFORMANCE REPORT")
print("-" * 40)

for student in students:
    print(
        f"{student['name']}: "
        f"Average = {student['average']:.2f}, "
        f"Grade = {student['grade']}"
    )

class_average = sum(
    student["average"] for student in students
) / len(students)

top_student = max(
    students,
    key=lambda student: student["average"]
)

print("-" * 40)
print(f"Class Average: {class_average:.2f}")
print(
    f"Top Performer: {top_student['name']} "
    f"({top_student['average']:.2f})"
)