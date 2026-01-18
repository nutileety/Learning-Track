# create the list
# create variable of increase count initialize to 0
# create variable of decrease count initialize to 0
# iterate the elements of list from start to second last
#   if the next element is greater than current 
#       increase variable count by 1
#   else the next elements is lesser than current 
        # then decrease variable count by 1
# print increase variable no. of counts
# print decrease variable no. of counts

arr = [1, 3, 2, 4, 3]
increase_count = 0
decrease_count = 0

for i in range(len(arr) - 1):
    if arr[i+1] > arr[i]:
        increase_count += 1
    elif arr[i+1] < arr[i]:
        decrease_count += 1
    
print(increase_count)
print(decrease_count)