# Create a list
# Iterate through the list using index from the first element to the second last element:
#     Compare the current element with the next element
#     If the current element is greater than the next element:
#         Print False and stop
# If all elements are checked without finding any violation:
#     Print True

arr = [1, 3, 4]
isSorted = True
for i in range(len(arr) - 1):
    if arr[i] > arr[i+1]:
        isSorted = False
        break

print(isSorted)
    