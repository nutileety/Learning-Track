users={
    'aeinstien':{
                'firstname':'albert',
                'secondname':'einstien',
                'location':'new york'
                },
    'mcurie':{
            'firstname':'merry',
            'secondname':'curie',
            'location':'united states'
            }
    }
for user,info in users.items():
    print(user)
    print(info['firstname'])
# for username,user_info in users.items():
#     full_name = f"{user_info['firstname']} {user_info['secondname']}"
#     location = user_info['location']
#     print(f"The {username} details is:")
#     print(f"\t Full name : {full_name.title()}")
#     print(f"\t Location : {location.title()}")