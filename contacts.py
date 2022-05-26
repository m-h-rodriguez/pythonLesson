contacts = {
    "number":4, 
    "students":
    [
        {"name":"Michelle Rodriguez", "email":"michelle@example.com"},
        {"name":"Harry Potter", "email":"harry@example.com"},
        {"name":"Hermione Granger", "email":"hermione@example.com"},
        {"name":"Ron Weasley", "email":"ron@example.com"}
    ]

}

for student in contacts["students"]:
    print(student["email"])

