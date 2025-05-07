# This is first version of this code about meows

# class Cat:
#     MEOWS = 3 
    
#     def meow(self):
#         for _ in range(self.MEOWS):
#             print("meow")
            
# cat = Cat()
# cat.meow()

# this is second version of this code about meows
def meow(n: int) -> None:
    for _ in range(n):
        print("meow")
      
number: int = int(input("Number of meows: "))
meows: str = meow(number)

print(meows) 