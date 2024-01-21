from pathlib import Path
import json

username = input("Enter your name: ")
path = Path('username.json')
content = json.dumps(username)
path.write_text(content)
print(f"Thank you {content} for entering your name!")
