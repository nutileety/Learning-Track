# create variable to intialize string variable
# 

word = 'education'
# vowels = ['a', 'e', 'i', 'o', 'u']
vowels = 'aeiou'
count = 0
for i in word:
    if i in vowels:
        count += 1
print(count)
