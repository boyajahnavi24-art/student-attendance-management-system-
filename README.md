# Student Attendance Management System

A beginner-friendly Python project for managing student attendance. It runs in the terminal and stores data in CSV files, so no extra Python packages are required.

## Features

- Add students with a unique student ID
- View the student list
- Mark students present or absent for the current date
- View saved attendance records
- Calculate a student's attendance percentage
- Save records between runs using CSV files

## Requirements

- Python 3.8 or newer
- No external packages required

## How to run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python main.py
   ```

   On some computers, use `python3 main.py` instead.

## How to use

1. Select **1** to add students.
2. Select **2** to view the student list.
3. Select **3** to mark today's attendance. Enter `P` for Present or `A` for Absent.
4. Select **4** to see attendance records.
5. Select **5** and enter a student ID to calculate the attendance percentage.
6. Select **6** to exit.

The program creates `students.csv` and `attendance.csv` automatically the first time it runs. These files hold the saved data.

## Project files

- `main.py` — the main Python program
- `students.csv` — student details (created automatically)
- `attendance.csv` — attendance records (created automatically)
- `requirements.txt` — package requirements (none needed)

## Attendance percentage

Attendance percentage is calculated as:

`(number of classes present / total classes recorded) × 100`

## Possible future improvements

- Add a graphical user interface (GUI)
- Use SQLite or MySQL for storage
- Add monthly attendance reports
- Add login for teachers
- Export reports to PDF

## Learning goals

This project practices Python functions, loops, conditionals, lists, dictionaries, file handling, CSV data, and basic validation.
