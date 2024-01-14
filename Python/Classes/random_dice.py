from random import randint

class Die:
    def __init__(self,sides=6):
        self.sides = sides

    def roll_dice(self):
        dices_number = randint(1,self.sides)
        return dices_number

# rolling of the 6 sided dice 10 rolls.
die6 = Die()
results = []
for result in range(10):
    result = die6.roll_dice()
    results.append(result)
print("\n The 6 sided rolls 10 times")
print(results)

# rolling of the 10 sided dice 10 rolls.
die10 = Die(sides=10)
results = []
for result in range(10):
    result = die10.roll_dice()
    results.append(result)
print("\n The 10 sided rolls 10 times")
print(results)

# rolling of the 6 sided dice 10 rolls.
die20 = Die(sides=20)
results = []
for result in range(10):
    result = die6.roll_dice()
    results.append(result)
print("\n The 20 sided rolls 10 times")
print(results)
