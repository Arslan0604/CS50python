# This is first version of this code about meows

# class Cat:
#     MEOWS = 3 
    
#     def meow(self):
#         for _ in range(self.MEOWS):
#             print("meow")
            
# cat = Cat()
# cat.meow()

# this is second version of this code about meows
def meow(n: int) -> str:
    """
    Meow n times.
    
    :param n: Number of meows
    :type n: int
    :raise ValueError: if n is negative
    :return: A string of n meows, one per line
    :rtype: str
    """
    return "meow\n" * n

      
number: int = int(input("Number of meows: "))
meows: str = meow(number)

print(meows, end="")
 