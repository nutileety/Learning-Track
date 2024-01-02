people=[]
chamsworth={
    'first_name':'Chris',
    'last_name':'Hamsworth',
    'age':35,
    'city':'New York'
    }
jbesoz={
    'first_name':'jeff',
    'last_name':'besoz',
    'age':45,
    'city':'paris'
    }
emosk={
    'first_name':'elon',
    'last_name':'mosk',
    'age':42,
    'city':'u s a'
    }

people.append(chamsworth)
people.append(jbesoz)
people.append(emosk)
# print(people)

print("The list of user are :")
for peoples in people:
    name=f"{peoples['first_name'].title()} {peoples['last_name'].title()}"
    age=peoples['age']
    city=peoples['city'].title()

    print("\tName :",name)
    print("\tAge :",age)
    print("\tCity :",city,"\n")