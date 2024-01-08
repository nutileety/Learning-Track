def formatted_name(firstname,lastname):
    fullname = f"{firstname} {lastname}"
    return fullname.title()

while True:
    print('\n(Enter "q" if you want to quit)')
    
    first = input('Enter the first name: ')
    if first == 'q':
        break

    last = input('Enter the last name: ')
    if last == 'q':
        break

    output = formatted_name(first,last)
    print("\nHello!",output)