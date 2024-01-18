print("Enter the number for calculations:")
print("(If you want to exit the calculations type 'q')")
while True:
    first_no = input('Enter the first number: ')
    if first_no == 'q':
        break

    second_no = input('Enter the second number: ')
    if second_no == 'q':
        break
    
    try:
        answer = int(first_no) / int(second_no)
    except ZeroDivisionError:
        print("The number can't be divided by zero")
    else:
        print("The answer is:",answer)