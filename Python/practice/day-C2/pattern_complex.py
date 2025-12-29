# repeat i from 1 to 5:
    # repeat j from 0 to i;
        # if (i+j) even :
            # print 1
        # else 
            # print 0
    # print space

for i in  range(1, 5):
    for j in range(1, i+1):
        if (i+j)%2 == 0:
            print(1, end='')
        else:
            print(0, end='')
    print()