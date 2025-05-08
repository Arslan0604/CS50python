# first, _ = input("what's your name? ").split(" ")
# print(f"Hello, {first}")


# unpacking process below
# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts


# # coins = [100, 50, 25]
# # print(total(*coins), "Knuts")

# # old school unpacking

# coins = {"galleons": 100, "sickles": 50, "knuts": 25}
# print(total(**coins), "Knuts")

def f(*args, **kwargs):
    print("Named:", kwargs)
    
    
f(galleons=100, sickles=50, knuts=25)
