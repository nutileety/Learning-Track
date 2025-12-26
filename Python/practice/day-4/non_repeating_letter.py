# create a string variable 
# create a empty dictionary variable
# iterate through each string variable:
#   if letter is not in dict:
#       add the letter as key to dictionary and count one as value
#   else
#       update the current letter of a dictionary by value count one 
#   print the letter which value is only one

letters = 'aabbbccccd'
countDict = {}
nonRepeat = ''
for i in letters:
    if i not in countDict:
        countDict[i] = 1
    else:
        countDict[i] +=1
    
for i in letters:
    if countDict[i] == 1:
        print(i)
        break
