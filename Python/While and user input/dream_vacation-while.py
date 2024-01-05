result = {}
while True:
    name = input("Your good name please: ")
    dream_vacation = input("hey which is your dream vacation: ")
    #appending to the result.
    result[name]=dream_vacation

    repeat = input("Are you want to enter the dream vacation once again (y/n):")
    if repeat == "n":
        break
print("\n------Result------")
for name,spot in result.items():
    print(f"* {name.title()} want to visit {spot.title()} once in life time.")