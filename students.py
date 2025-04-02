# with open("students.csv") as file:
#     for line in file:
#         name, house  = line.rstrip().split(",")
#         print(f"{name} is in {house}")

students = []

with open("students.csv") as file:
    for line in file:
        name, home = line.rstrip().split(",")
        student = {"name": name, "home": home}

        students.append(student)
        

        
for student in sorted(students, key=lambda student: student['name']):
    print(f"{student['name']} is from {student['home']}")
        
        
