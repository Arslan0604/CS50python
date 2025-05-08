# This is first version of this code about meows

# class Cat:
#     MEOWS = 3 
    
#     def meow(self):
#         for _ in range(self.MEOWS):
#             print("meow")
            
# cat = Cat()
# cat.meow()

# this is second version of this code about meows
# def meow(n: int) -> str:
#     """
#     Meow n times.
    
#     :param n: Number of meows
#     :type n: int
#     :raise ValueError: if n is negative
#     :return: A string of n meows, one per line
#     :rtype: str
#     """
#     return "meow\n" * n

      
# number: int = int(input("Number of meows: "))
# meows: str = meow(number)

# print(meows, end="")
 
# import sys
 
# if  len(sys.argv) == 1:
#      print("meow")
# elif len(sys.argv) == 3 and sys.argv[1] == "-n":
#     n = int(sys.argv[2])
#     for _ in range(n):
#         print("meow")
# else:
#      print("usage: meows.py")


# other version of the code
import argparse

parser = argparse.ArgumentParser(description="Meow line a cat")
parser.add_argument("-n", help="number of times to meow")
args = parser.parse_args()

for _ in range(int(args.n)):
     print("meow")
     
 