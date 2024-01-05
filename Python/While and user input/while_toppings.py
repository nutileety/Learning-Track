toppings=""
active =True
while active:
    toppings = input("Which toppings you have to add: ")
    if toppings != 'quit': 
        print(toppings,"toppings are added")
    else:
        active = False
    