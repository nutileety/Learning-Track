# Find the maximum sum of any contiguous subarray of size k

# Create an array of numbers
# Create a variable k to represent the size of the subarray

# Calculate the sum of the first k elements of the array
# Store this sum as the current window sum
# Set this sum as the maximum sum initially

# Iterate through the array starting from index k to the end:
#     Add the current element to the window sum
#     Subtract the element that is moving out of the window
#     Compare the updated window sum with the maximum sum
#     Update the maximum sum if the current window sum is greater

# After the loop, print the maximum sum

arr = [2, 1, 5, 1, 3, 2]
k = 3

# current_sum = sum(arr[:3])
current_sum = 0
for i in range(0, k):
    current_sum += arr[i]
max_sum = current_sum

for i in range(k, len(arr)):
    current_sum += arr[i]
    current_sum -= arr[i-k]
    if current_sum > max_sum:
        max_sum = current_sum

print(max_sum)

