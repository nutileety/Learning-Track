from pathlib import Path
import json

def write_number():
    number = input("Enter your favarite number: ")
    path = Path('Fav_number.json')    
    content = json.dumps(int(number))
    path.write_text(content)

write_number()

