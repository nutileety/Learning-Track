# create variable of number list
# create left variable to array index 0 as the start of list
# create right varialbel to array index len - 1 as end value of the list
# repeat with checking condition that left should less than right
#   perform swaping the left as right and right as left with help of temp variable
#   then increment the left by 1 and decrement right by -1
#   when condition checks for left is greater than right loop stops 
# print the reverse array

arr = [5, 6, 7, 8]
left = 0
right = len(arr)-1
while left < right: 
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp
    left = left + 1
    right = left - 1
print(arr)