current_users=['admin','Ram','raj','john','suhil']
new_users=['ragav','tej','ram','Raj','tom']
user_lower=[user.lower() for user in current_users]
#OR
# user_lower=[]
# for user in current_users:
#     user_lower.append(user.lower())
# print(user_lower)
for new_user in new_users:
    if new_user.lower() in user_lower:
        print(f"The {new_user} name is already used!")
    else:
        print(f"You can use this name")