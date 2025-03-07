
# # Ask user for their name
# name = input("What is your name? ")

# # Say hello to user
# print("Hello, " + name + "!")

# # Ask user for their age
# age = input("How old are you? ")

# # Say how old user will be in 10 years
# age = int(age) + 10 

# print("In 10 years, you will be " + str(age) + " years old!")


# # # Ask user for their name
# name = input("What is your name? ").strip().title()

# # Remove whitespace from str and capitalize first letter
# # name = name.strip().title()
# first, last = name.split()

# # Say hello to user
# print(f"Hello! {first}")

def main():
    name = input("What's your name? ")
    hello(name)
  
def hello(to="world"):
    print("hello,", to)
    
main()


