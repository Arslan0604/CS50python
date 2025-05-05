students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Luna", "house": "Ravenclaw"},
    {"name": "Cedric", "house": "Hufflepuff"},
]

houses = set()
for student in students:
    houses.add(student["house"])
        
for house in houses:
    print(house)