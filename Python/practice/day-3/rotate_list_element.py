# create a list 
# create left variable to 0th index
# create next variable to 1st index
# iterate until left equal lenght of list
#   swap the left to next with temp variable
#   increase left by 1 
#   increase next by 1
#   when left is equal to the list lenght the loop stops
# print the list

arr = [1, 2, 3, 4]
temp = arr[0]
for i in range(0, len(arr)-1):
    arr[i] = arr[i+1]
arr[len(arr)-1] = temp
print(arr)