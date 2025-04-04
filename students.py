# with open("students.csv") as file:
#     for line in file:
#         name, house  = line.rstrip().split(",")
#         print(f"{name} is in {house}")

# import csv


# students = []

# with open("students.csv") as file:
#     reader = csv.reader(file)
#     for name, home in reader:
#         students.append({"name": name, "home": home}) 
        
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")


# this is another way to solve it with Dictionery 

# import csv
# students = []

# with open("students.csv") as file:
#     reader = csv.DictReader(file)
    
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"]})
        
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")
    
    
# import csv

# name = input('What is your name? ')
# home = input('Where is your home? ')

# with open("students.csv", "a") as file: # v csv zapisyvaetsya 
#     writer = csv.writer(file)
#     writer.writerow([name, home])
    
import csv

name = input('What is your name? ')
home = input('Where is your home? ')

with open("students.csv", "a") as file: # v csv zapisyvaetsya 
    writer = csv.DictWriter(file, fieldnames=['name', 'home'])
    writer.writerow({'name': name , 'home': home})   

    