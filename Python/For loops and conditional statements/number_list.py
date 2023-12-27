squares=[]
for value in range(1,11):
    # values=value**2
    # print(values)
    squares.append(value**2)
print(squares)

#List comperhension
squares=[value**2 for value in range(11)]
print(squares)