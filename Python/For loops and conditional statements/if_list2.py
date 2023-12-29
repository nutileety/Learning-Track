toppings=['mashroom','onion','green pepper']
for topping in toppings:
    if topping=='green pepper':
        print("sorry, green pepper is not avilable")
    else:
        print(f"adding {topping}")

#if has for loop
request_toppings=["Onion"]
  
if request_toppings:
    for topping in request_toppings:  
        print(f"{topping} is adding")
else:
    print("Do you really want a pizza without toppijngs!")