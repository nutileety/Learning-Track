try:
    a = int(input('enter first number: '))
    b = int(input('enter second number: '))
    add = a + b
except ValueError:
    print('Please enter only numbers!')
else:
    print('Addition =',add)