url = input("URL: ").strip()

username = url.replace("https://github.com/", "")

print(f"Username: {username}")