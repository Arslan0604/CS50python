import re

email = input("What is you email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid email")
else:
    print("INvalid email")
