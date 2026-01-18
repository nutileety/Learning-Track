# Create a list of numbers
# Create a variable count and initialize it to 0

# Iterate through the list from the first index to the second last index:
#     Compare the current element with the next element
#     If the next element is greater than the current element:
#         Increase the count by 1

# After the loop, print the count

arr = [1, 2, 2, 4, 3]
count = 0

for i in range(len(arr) - 1):
    if arr[i+1] > arr[i]:
        count += 1

print(count)
