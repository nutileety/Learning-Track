
while True :
    age=input("what is your age:")
    
    if age == 'quit':
        break

    age=int(age)
    if age < 3:
        print("we don't charge for age below 3")
    elif age < 12:
        print(f" your age is {age} So, you have to pay ₹10")
    else:
        print(f"your age is {age} So, you have to pay ₹15")
