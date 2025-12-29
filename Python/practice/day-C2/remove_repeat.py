# create an string variable
# create and empty set
# create empty string variable to store the non repeated string
# iterate through the string variable
    # if i is not in set:
        # add i to set
        # store it in the empty string varible
# print non repeated string

words = 'programming'
tempSet = set()
noRepeat = ''
for i in words.lower():
    if i not in tempSet:
        tempSet.add(i)
        noRepeat += i
print(noRepeat)