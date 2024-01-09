def my_profile(first_name,last_name,**profile):
    print("This is my profile :")
    profile['firstname'] = first_name
    profile['lastname'] = last_name
    print(profile)

my_profile('john','wick',location = 'New York',designation = 'Gangster',
           car = 'Mustang')