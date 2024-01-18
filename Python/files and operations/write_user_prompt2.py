from pathlib import Path

path = Path('guest_book.txt')
users = []
while True:
    names = input('enter the name: ')
    if names == 'quit':
        break
    users.append(names)

names_str = ''
for names in users:
    names_str += f"{names}\n"
path.write_text(names_str)