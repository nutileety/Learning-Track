# create an list of numbers
# create variable assigned by the value of first list number arr[0]
# iterate through list
# compare array of i with the first list number
#   if the array of i is greater than the first element 
#       then then the max number is array of i
# print the max value of the array 

arr = [3, 1, 7, 2, 5]
maxNum = arr[0]
for i in arr:
    if i > maxNum:
        maxNum = i
print(f'Maximum value in the list is: {maxNum}')