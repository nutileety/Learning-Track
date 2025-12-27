# create a string varible
# create an variable having vowels
# create count variable to 0
# iterate through the string by converting to lower
    # if the iterated value is not in vowels
        # then count as 1
# print the number of consonants

words = 'I am the Zen practitioner'
vowels = 'aeiou'
count = 0
for char in words.lower():
    if char not in vowels and not char.isalpha():
        count += 1
print(f'The number of Consonants are: {count}') 