def make_pizza(size,*toppings):
    print(f"\nThe {size} inches toppings are:")
    for topping in toppings:
        print("-",topping)

make_pizza(16,'pepperoni')
make_pizza(12,'onion','cheese','corn')