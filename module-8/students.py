#Ryan Barber Assignment 8.2 2/22/26

import json
from pathlib import Path

def print_students(student_list):
    for s in student_list:
        print(f"{s['F_Name']} {s['L_Name']} : ID = {s['Student_ID']}, Email = {s['Email']}")


def main():
    filename = Path(__file__).with_name("Student.json")
    print("Using JSON file:", filename)

    with open(filename, "r", encoding="utf-8") as f:
        students = json.load(f)

    unique = {}
    for s in students:
        unique[s["Student_ID"]] = s
    students = list(unique.values())

    print("This is the original Student list.\n")
    print_students(students)

    new_student = {
        "F_Name": "Ryan",
        "L_Name": "Barber",
        "Student_ID": 99999,
        "Email": "ryanbarber@gmail.com"
    }
    if 99999 not in [s["Student_ID"] for s in students]:
        students.append(new_student)

    print("\nThis is the updated Student list.\n")
    print_students(students)

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(students, f, indent=4)

    print("\nThe student.json file was updated.\n")


if __name__ == "__main__":
    main()
