from pathlib import Path
import json

def read_text(pathname):
    path = Path(pathname)
    content = path.read_text()
    json.loads(content)
    return content

value = read_text('fav_number.json')
print(f"I know your favrite number is : {value}")