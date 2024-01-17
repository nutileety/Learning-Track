from pathlib import Path

name = input('Enter your name: ')
path = Path('guest.txt')
path.write_text(name)
print(f'The name is written to the file: {path}')