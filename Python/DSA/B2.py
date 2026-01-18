# create the list
# create count variable
# iterate through the second last elements of list 
#   if the next element is lesser than the current
#       increase the count by 1
# print the no of counts calculated during the iteration

arr = [5, 3, 3, 2, 4]
count = 0
for i in range(len(arr) - 1):
    if arr[i+1] < arr[i]:
        count += 1

print(count)