numbers=[]
for value in range(1000000):
    numbers.append(value)
# print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#odd numbers from 1-20
for number in range(1,20,2):
    print(number)

#multiple of 3 from 3-30
for multi in range(3,31,3):
    print(multi)

# cube from 1-10

for value in range(1,11):
    cube=value**3
    print(f"{value} cube is {cube}")

#above cube in list comperhension
cube=[value**3 for value in range(1,11)]
print(cube)
#or
print([value**3 for value in range(1,11)])