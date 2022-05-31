def load_students():
    students = [
        {
            "fname": "Adrienne",
            "lname": "Adams",
        },
        {
            "fname": "Doug",
            "lname": "Wiley",
        },
        {
            "fname": "Emily",
            "lname": "Coleman",
        },
        {
            "fname": "Grace",
            "lname": "Ensign",
        },
        {
            "fname": "Katie",
            "lname": "Cook",
        },
        {
            "fname": "Kimberly",
            "lname": "B",
        },
        {
            "fname": "Mariah",
            "lname": "Corso",
        }
    ]
    return(students)


def standup(students):
    for student in students:
        print("Hello " + student["fname"] + " " + student["lname"])
        input("What did you work on last week?")
        print(f"Thanks so much {student['fname']}")


def main():
    standup(students)
    students = load_students()


if __name__ == "__main__":
    main()
