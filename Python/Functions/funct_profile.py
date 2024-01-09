def make_profile(first_name,last_name,**user_details):
    user_details['first']=first_name
    user_details['last']=last_name
    return user_details

make = make_profile('albert','einstein',location = 'bangaluru',country = 'India')
print(make)