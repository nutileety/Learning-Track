from pathlib import Path
import json

def greet_user():
    path = Path('username1.json')
    username = get_stored_user(path)
    if username:
        print("welcome back!",username)
    else:
        content = get_username(path)
        print(f"Thank you {content} for entering name")

def get_stored_user(path):
    if path.exists():
        content = path.read_text()
        username = json.loads(content)
        return username
    else:
        return None
    
def get_username(path):
    username = input("Enter your name: ")
    content = json.dumps(username)
    username = path.write_text(content)
    return username

greet_user()

# if path.exists():
#     content = path.read_text()
#     username = json.loads(content)
#     print(f"Welcome back! {username.title()}")
# else:
#     username = input('Enter your name: ')
#     content = json.dumps(username)
#     path.write_text(content)
#     print(f"Thank you {username.title()} for writing your name!")