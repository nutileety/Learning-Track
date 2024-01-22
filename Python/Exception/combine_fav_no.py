from pathlib import Path
import json

path = Path('fav_number1.json')
try:    
    content = path.read_text()
except FileNotFoundError:
    number = input("Enter your favarite number: ")
    content = json.dumps(int(number))
    path.write_text(content)
else:
    json.loads(content)
    print(f"Your favrite number is : {content}")

    
