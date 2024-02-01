# squares = []
# for value in range(1,11):
#     square=value**2
#     squares.append(square)
#     print(squares,square)
#     # print(value)

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
# aliens = [alien_0, alien_1, alien_2]
# # print(aliens)
# for alien in aliens:
#     print(alien)

# aliens = []
# # Make 30 green aliens.
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed':'slow'}
#     aliens.append(new_alien)

# # print(aliens[:5])
# # Show the first 5 aliens.
# for alien in aliens[:5]:
#     print(alien)
# print("...")
# # Show how many aliens have been created.
# print(f"Total number of aliens: {len(aliens)}")

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit',
'cat']
print(pets)
for cat in pets:
    if cat == 'cat':
        pets.remove('cat')
print(pets)