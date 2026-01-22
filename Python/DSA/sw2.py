# Smallest Subarray with Sum ≥ Target

# Create a list of numbers
# Create a target value

# Initialize left pointer to 0
# Initialize current sum to 0
# Initialize minimum length to infinity (or a very large number)

# Iterate right pointer from 0 to end of the array:
#     Add the element at right to the current sum

#     While the current sum is greater than or equal to the target:
#         Calculate the current window length
#         Update the minimum length if this window is smaller
#         Subtract the element at left from the sum
#         Move left pointer to the right

# If no valid window was found:
#     Return 0
# Else:
#     Return the minimum length

# | Step | right | left | Action | Added | Removed | current_sum | Window (indexes) | Window elements | Window length | min_length |
# | ---: | ----: | ---: | ------ | ----: | ------: | ----------: | ---------------- | --------------- | ------------- | ---------- |
# |    0 |     — |    0 | start  |     — |       — |           0 | —                | —               | —             | ∞          |
# |    1 |     0 |    0 | expand |     2 |       — |           2 | [0–0]            | [2]             | 1             | ∞          |
# |    2 |     1 |    0 | expand |     3 |       — |           5 | [0–1]            | [2,3]           | 2             | ∞          |
# |    3 |     2 |    0 | expand |     1 |       — |           6 | [0–2]            | [2,3,1]         | 3             | ∞          |
# |    4 |     3 |    0 | expand |     2 |       — |           8 | [0–3]            | [2,3,1,2]       | 4             | 4          |
# |    5 |     3 |    1 | shrink |     — |       2 |           6 | [1–3]            | [3,1,2]         | 3             | 4          |
# |    6 |     4 |    1 | expand |     4 |       — |          10 | [1–4]            | [3,1,2,4]       | 4             | 4          |
# |    7 |     4 |    2 | shrink |     — |       3 |           7 | [2–4]            | [1,2,4]         | 3             | 3          |
# |    8 |     4 |    3 | shrink |     — |       1 |           6 | [3–4]            | [2,4]           | 2             | 3          |
# |    9 |     5 |    3 | expand |     3 |       — |           9 | [3–5]            | [2,4,3]         | 3             | 3          |
# |   10 |     5 |    4 | shrink |     — |       2 |           7 | [4–5]            | [4,3]           | 2             | 2          |
# |   11 |     5 |    5 | shrink |     — |       4 |           3 | [5–5]            | [3]             | 1             | 2          |


arr = [2, 3, 1, 2, 4, 3]
# arr = [1, 1, 1, 1, 1, 1]
target = 7

left = 0
current_sum = 0
min_len = float('inf')

for right in range(0, len(arr)):
    current_sum += arr[right]

    while current_sum >= target:
        window_length = right - left + 1
        min_len = min(min_len, window_length)
        current_sum -= arr[left]
        left += 1
    
if min_len == float('inf'):
    print(0)
else:
    print(min_len)
