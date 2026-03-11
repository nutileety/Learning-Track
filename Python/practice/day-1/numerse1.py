# number of row: 4
# repeat i from 1 to 4 
#   repeat j time of i from 0 to i
#       print i
# print newline

for i in range(1, 5):
    for j in range(0, i):
        print(i, end='')
    print()


# number of row: 4
# repeat i from 1 to 4 
#   convert i to string and multiply i times to the string
# print newline

for i in range(1, 5):
    print(str(i) * i)
    