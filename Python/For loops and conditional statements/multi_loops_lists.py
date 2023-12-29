avilable_toppings=['onion','corn','mashroom']
requested_toppings=['pepperoni','onion','cheese']
for requested_topping in requested_toppings:
    if requested_topping in avilable_toppings:
        print(f"{requested_topping} is adding") 
    else:
        print(f"your {requested_topping} toppings is not avilable")