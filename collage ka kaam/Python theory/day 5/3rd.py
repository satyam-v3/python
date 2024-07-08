# Write a Python program to display the examination schedule.

def print_exam_schedule(exam_schedule):
    print("Exam Schedule:")
    for subject, date_time in exam_schedule.items():
        print(f"{subject}: {date_time}")

def main():
    exam_schedule = {
        "Math": "May 10, 2024 - 9:00 AM",
        "History": "May 12, 2024 - 10:30 AM",
        "Science": "May 15, 2024 - 1:00 PM"
    }
    print_exam_schedule(exam_schedule)

if __name__ == "__main__":
    main()