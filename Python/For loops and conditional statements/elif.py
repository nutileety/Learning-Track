age=12
if age<=4:
    prise=0
elif age<=12:
    prise=25
elif age<=45:
    prise=40
elif age>45:
    prise=20

print(f"you {age} have to pay ₹{prise}")