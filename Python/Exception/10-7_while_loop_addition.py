print("if you want to quit enter 'q'")
while True:
    try:
        first_no = input("Enter first number: ")
        if first_no == 'q':
            break
        
        second_no = input("Enter second number: ")
        if second_no == 'q':
            break

        add = int(first_no) + int(second_no)
    
    except ValueError:
        print('Please enter only numbers to calculate!')
    else:
        print("Addition :",add)
    
