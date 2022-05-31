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

for s in students:
    print("Hello " + s["fname"] + " " + s["lname"])
    input("What did you work on last week?")
    print(f"Thanks so much {s['fname']}")
