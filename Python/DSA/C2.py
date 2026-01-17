# Create a list
# Create a variable left to track the position to place the next non-zero element

# Iterate through the list using a variable right that scans every element:
#     If the element at right is not zero:
#         Assign that element to the position at left
#         Increment left by 1

# After finishing the iteration:
#     The remaining positions from left to end of the list should be set to zero

arr = [0, 1, 0, 3, 12]
left = 0

for right in range(len(arr)):
    if arr[right] != 0:
        arr[left] = arr[right]
        left += 1

for i in range(left, len(arr)):
    arr[i] = 0

print(arr)