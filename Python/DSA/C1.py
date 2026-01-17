# create a list
# create variable assgin the first index as left
# create variable assgin the last index as right
#  repeate loop until the left > right
#  swap the values of each with temprary variable
#   icrement the left by 1 
#   decreament the right by 1
# repeat loop until the left become greater than right

# print the reversed array

arr = [1, 2, 3, 4]
left = 0
right = len(arr) - 1

while left < right:
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp
    left += 1
    right -= 1

print(arr)