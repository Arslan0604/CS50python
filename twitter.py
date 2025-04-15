import re


url = input("URL: ").strip()

# username = url.replace("https://github.com/", "")

# username = url.removeprefix("https://github.com/")

if matches := re.search(r"^https?://(?:www\.)?github\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    
    print(f"Username:", matches.group(1))
