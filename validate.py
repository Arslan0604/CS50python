import re

email = input("What is you email? ").strip()

if re.search(r"^.+@.+\.edu$", email):
    print("Valid email")
else:
    print("INvalid email")

