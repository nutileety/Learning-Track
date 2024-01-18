from pathlib import Path

path = Path('alice.txt')
try:
    content = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print('The file is not found which you are looking for!')
else:
    print(content)
