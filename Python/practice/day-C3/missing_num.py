# create list of numbers
# find the length of the list

# repeat element from 0 to length + 1 times
    # calculate the expected sum 

# repeat element from list:
    # calculate the actual sum

# result to substract actual sum from expected sum
# print the result

list1 = [1, 2, 3, 5]
length = len(list1)

expected_sum = 0
for i in range(1, length + 2):
    expected_sum += i


actual_sum = 0
for j in list1:
    actual_sum += j


result = expected_sum - actual_sum
print(f'The Missing numbers is: {result}')
