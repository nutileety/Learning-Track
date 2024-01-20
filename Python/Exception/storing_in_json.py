from pathlib import Path
import json

numbers = [12,4,5,88,99,100]
path = Path('numbers.json')
content = json.dumps(numbers)
path.write_text(content)

content = path.read_text()
printing = json.loads(content)
print(printing)