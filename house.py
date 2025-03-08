name = input("What is your name? ")

# if name == "Harry" or name == "Hermione" or name == "Ron":
#     print("Gryffindor!")
# elif name == "Draco":
#     print("Slytherin!")
# else:
#     print("Who?")

# another way to write the above code is:

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor!")
    case "Draco":
        print("Slytherin!")
    case _:
        print("Who?")