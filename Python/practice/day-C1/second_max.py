# create a list variable 
# assume first element as largest
# assume second elementas second largest

# if the second is larger than largest 
# swap

# iterate through the list
#   if the iterated element is larger
        # than largest will be second largest
        # than the iterated element is largest
    # elif the iterated element is lesser than largest and greater than second largest
        # than iterated element is second largest
# print second largest

num = [3, 4, 7, 2, 5]
maxNum = num[0]
secondMax = num[1]

if secondMax > maxNum:
    temp = secondMax
    secondMax = maxNum
    maxNum = temp

for i in num[2:]:
    if i > maxNum:
        secondMax = maxNum
        maxNum = i
    elif i < maxNum and i > secondMax:
        secondMax = i
print(f'The second largest number is: {secondMax}')


