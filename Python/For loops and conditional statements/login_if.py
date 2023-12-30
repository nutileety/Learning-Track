users=['admin','ram','raj','tej','john']
users.clear()
if users:
    for user in users:
        if user=='admin':
            print(f"Hello {user.title()}, Would you like to see the status.")
        elif user:
            print(f"Hello {user.title()}, Welcome to our website.")
else:
    print("We need some users")