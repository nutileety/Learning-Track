# Create a list of numbers
# Create a variable k

# Initialize left pointer to 0
# Create an empty dictionary to store frequency of elements
# Initialize max_length to 0

# Iterate right pointer through the list:
#     Add the current element to the dictionary (increase its count)

#     While the number of distinct elements in the dictionary is greater than k:
#         Reduce the count of the element at left
#         If its count becomes zero, remove it from the dictionary
#         Move left pointer to the right

#     At this point, the window is valid
#     Calculate the current window length
#     Update max_length if the current window is larger

# After the loop, print max_length


arr = [1, 2, 1, 2, 3]
k = 2
left = 0
distincts = {}
max_length = 0

for right in range(len(arr)):
    if arr[right] not in distincts:
        distincts[arr[right]] = 1
    else:
        distincts[arr[right]] += 1

    while len(distincts) > k:
        distincts[arr[left]] -= 1
        if distincts[arr[left]] == 0:
            del distincts[arr[left]]
        left += 1

    window_lenth = right - left + 1
    if window_lenth > max_length:
        max_length = window_lenth

print(max_length)

     
