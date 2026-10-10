import csv
import os
from datetime import date

STUDENTS_FILE = "students.csv"
ATTENDANCE_FILE = "attendance.csv"


def create_file_if_missing(filename, headers):
    """Create a CSV file with headers if it does not exist."""
    if not os.path.exists(filename):
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(headers)


def setup_files():
    create_file_if_missing(STUDENTS_FILE, ["student_id", "name"])
    create_file_if_missing(ATTENDANCE_FILE, ["date", "student_id", "name", "status"])


def load_students():
    with open(STUDENTS_FILE, "r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def add_student():
    student_id = input("Enter student ID: ").strip()
    name = input("Enter student name: ").strip()

    if not student_id or not name:
        print("Student ID and name cannot be empty.")
        return

    students = load_students()
    if any(student["student_id"] == student_id for student in students):
        print("That student ID already exists.")
        return

    with open(STUDENTS_FILE, "a", newline="", encoding="utf-8") as file:
        csv.writer(file).writerow([student_id, name])

    print(f"Student '{name}' added successfully.")


def view_students():
    students = load_students()
    if not students:
        print("No students found. Add a student first.")
        return

    print("\n--- Student List ---")
    print(f"{'ID':<15}Name")
    print("-" * 35)
    for student in students:
        print(f"{student['student_id']:<15}{student['name']}")


def mark_attendance():
    students = load_students()
    if not students:
        print("No students found. Add students first.")
        return

    today = date.today().isoformat()
    print(f"\n--- Mark Attendance ({today}) ---")
    print("Enter P for Present or A for Absent.")

    with open(ATTENDANCE_FILE, "r", newline="", encoding="utf-8") as file:
        existing_records = list(csv.DictReader(file))

    for student in students:
        already_marked = any(
            record["date"] == today and record["student_id"] == student["student_id"]
            for record in existing_records
        )
        if already_marked:
            print(f"Attendance already recorded for {student['name']} today.")
            continue

        while True:
            status = input(f"{student['name']} ({student['student_id']}): ").strip().upper()
            if status in ("P", "A"):
                break
            print("Please enter P or A.")

        status_text = "Present" if status == "P" else "Absent"
        with open(ATTENDANCE_FILE, "a", newline="", encoding="utf-8") as file:
            csv.writer(file).writerow([today, student["student_id"], student["name"], status_text])

    print("Attendance session completed.")


def view_attendance():
    with open(ATTENDANCE_FILE, "r", newline="", encoding="utf-8") as file:
        records = list(csv.DictReader(file))

    if not records:
        print("No attendance records yet.")
        return

    print("\n--- Attendance Records ---")
    print(f"{'Date':<13}{'ID':<15}{'Name':<25}Status")
    print("-" * 65)
    for record in records:
        print(
            f"{record['date']:<13}{record['student_id']:<15}"
            f"{record['name']:<25}{record['status']}"
        )


def attendance_percentage():
    students = load_students()
    if not students:
        print("No students found. Add students first.")
        return

    student_id = input("Enter student ID to calculate percentage: ").strip()
    student = next((s for s in students if s["student_id"] == student_id), None)
    if student is None:
        print("Student ID not found.")
        return

    with open(ATTENDANCE_FILE, "r", newline="", encoding="utf-8") as file:
        records = [
            row for row in csv.DictReader(file)
            if row["student_id"] == student_id
        ]

    total = len(records)
    if total == 0:
        print("No attendance records for this student yet.")
        return

    present = sum(1 for record in records if record["status"] == "Present")
    percentage = (present / total) * 100

    print(f"\nStudent: {student['name']}")
    print(f"Classes recorded: {total}")
    print(f"Present: {present}")
    print(f"Attendance percentage: {percentage:.2f}%")


def main():
    setup_files()

    while True:
        print("\n====== Student Attendance Management System ======")
        print("1. Add student")
        print("2. View students")
        print("3. Mark attendance for today")
        print("4. View attendance records")
        print("5. Calculate attendance percentage")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            mark_attendance()
        elif choice == "4":
            view_attendance()
        elif choice == "5":
            attendance_percentage()
        elif choice == "6":
            print("Thank you for using the Attendance Management System!")
            break
        else:
            print("Invalid option. Please choose a number from 1 to 6.")


if __name__ == "__main__":
    main()
