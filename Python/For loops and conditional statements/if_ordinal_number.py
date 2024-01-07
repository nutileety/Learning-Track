ordinal_number=[1,2,3,4,5,6,7,8,9]
for number in ordinal_number:
    if number == 1:
        print(f"{number}st",end=", ")
    elif number == 2:
        print(f"{number}nd",end=", ")
    elif number == 3:
        print(f"{number}rd",end=", ")
    else:
        print(f"{number}th",end=", ")

print("\nDone")