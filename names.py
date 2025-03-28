
# names = []

# for _ in range(3):
#     names.append(input("What's your name? "))


# for name in sorted(names):
#     print(f"hello, {name}") 
    
  # this is giving you create txt file 3 line code below:
    
# name = input("What's your name? ")

# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

# other way of making a file: reload it not saving if 'r'

with open("names.txt", "r") as file:
    lines = file.readlines()
    
for line in lines:
    print("hello,", line.rstrip())
    
    





