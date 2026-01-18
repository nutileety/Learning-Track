# Create a list
# Create a variable that stores the value to remove
# Create a variable left that points to the position where the next valid element should go

# Iterate through the list using right:
#     If the element at right is not equal to the value to remove:
#         Assign that element to the position at left
#         Increment left

# After the loop:
#     The first left elements of the list are the result

arr = [3, 2, 2, 3]
left = 0
target = 3
for right in range(len(arr)):
    if arr[right] != target:
        arr[left] = arr[right]
        left += 1

print(arr[:left])