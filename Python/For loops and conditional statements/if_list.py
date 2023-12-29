cars=['mazda','bmw','audi','porshe','nissan']
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())

#comparing if in inequility
toppings='mushroom'
if toppings!='corn':
    print("Hold the corn toppings!")

#another !=
not_allowed=['rohan','rishi','jagan','mohan']
user1='ram'
if user1 not in not_allowed:
    print("can register")
