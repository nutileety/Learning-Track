from pathlib import Path
import json

def get_stored_user(path):
    if path.exists():
        content = path.read_text()
        user_info = json.loads(content)
        return user_info
    else:
        return None
    
def get_username(path):
    user_info = {}
    user_info['name'] = input("Enter your name: ").title()
    user_info['age'] = int(input("Enter your age: "))
    user_info['city'] = input("Enter your city: ").title()

    content = json.dumps(user_info)
    path.write_text(content)
    return user_info

def greet_user():
    path = Path('new_user_info.json')
    user_info = get_stored_user(path)
    
    if user_info:
        current = input(f"Are you a {user_info['name']}(y/n): ")
        if current == 'y':
            print("welcome back!",user_info['name'])
        else:
            user_info = get_username(path)
            print(f"Thank you {user_info['name']} for entering your details")
    else:
        user_info = get_username(path)
        print(f"Thank you {user_info['name']} for entering your details")

greet_user()
