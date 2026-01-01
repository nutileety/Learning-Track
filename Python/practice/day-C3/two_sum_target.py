# create an list of numbers
# create and target variable
# create empty directory to store the number and its index
# iterate throught the list with index and its current value
#   find needed num (by target - current value)
    # if needed number is in the dictionay:
        # then print the index number with its value
    # else
        # store the needed number in the dictionary with index

arr = [2, 7, 11, 15]
target = 9
dict_to_store = {}

for index, current_value in enumerate(arr):
    needed_num = target - current_value
    if needed_num in dict_to_store:
        print([dict_to_store[needed_num], index])
        break
    else:
        dict_to_store[current_value] = index