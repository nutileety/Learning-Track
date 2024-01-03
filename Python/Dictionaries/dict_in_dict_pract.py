users={}
users['aeinstien']={
                'firstname':'albert',
                'secondname':'einstien',
                'location':'new york'
                }
users['mcurie']={
            'firstname':'merry',
            'secondname':'curie',
            # 'location':'united states'
            }
    
# print(users)

for username,user_info in users.items():
    if  username == 'mcurie':
        print(f"{username.title()} details :")
        #adding location to the mcurie dictonary
        user_info['loacation']='united states'
        for key,value in user_info.items():
            print(f"\t- {key.title()} : {value.title()}")
    else:
        print(f"{username.title()} details :")
        for key,value in user_info.items():
            print(f"\t- {key.title()} : {value.title()}")


   
   
   
   
   
   
   
   
   
   
   
   
   
   
    # full_name = f"{user_info['firstname']} {user_info['secondname']}"
    # location = user_info['location']
    # print(f"The {username} details is:")
    # print(f"\t Full name : {full_name.title()}")
    # print(f"\t Location : {location.title()}")