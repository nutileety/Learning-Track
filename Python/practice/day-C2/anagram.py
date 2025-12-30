# create a string1(listen)
# create a string2(silent)
# create an empty dictionary

# if lenght of string1 not equal to the length string2
#   print false and stop
# else
    # iterate character from the string1:
    #   if the character is not in the dictionary
    #       add the character to dictionary and couter by 1
    #   else
    #       count that character by 1 

    # iterate character from the string2:
        # if the character is in the dictionary
            # sustracter the count of the character by 1
        # else
            # print false

    # iterate the dictionary 
        # if the the dictionary of value is not equals to 0 
            # than print false

    # print false

s1 = 'listen'
s2 = 'silent'
dictToCheck = {}

if len(s1) != len(s2):
    print(False)
else:
    for char1 in s1:
        if char1 not in dictToCheck:
            dictToCheck[char1] = 1
        else:
            dictToCheck[char1] += 1

    isAnagram = True
    
    for char2 in s2:
        if char2 not in dictToCheck:
            isAnagram = False
            break
        else:
            dictToCheck[char2] -= 1

    for i in dictToCheck:
        if dictToCheck[i] != 0:
            isAnagram = False
            break
    print(isAnagram)