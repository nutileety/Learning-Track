def sandwich(*toppings):
    print("\nI want this toppings on my sandwich are:")
    for topping in toppings:
        print(f"* {topping}")

sandwich('onion','tomato','extra spies')
sandwich('corn','bread crumbs')
sandwich('pepperoni','cheese','chasews','spieces')