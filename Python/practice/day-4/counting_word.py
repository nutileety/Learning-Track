# create an variable of string
# create empty dictionary varible
# iterate the string variable 
#   if letter is not in dictionary
#       add letter as key and its count one as value
#   else
#       update the existing to count one
# print the dictionary

letters = 'aabbbcccc'
countDict = {}
for i in letters:
    if i not in countDict:
        countDict[i] = 1
    else:
        countDict[i] +=1
print(countDict)