# class Cat:
#     MEOWS = 3 
    
#     def meow(self):
#         for _ in range(self.MEOWS):
#             print("meow")
            
# cat = Cat()
# cat.meow()

def meow(n: int):
    for _ in range(n):
        print("meow")
      
number: int = int(input("Number of meows: "))
meow(number)