cars=['audi','benz','mazda','dodge']
print("cars=='lambo', I predicted false")
print(cars=='lambo')

print("cars[0]=='audi',I predict true")
print(cars[0]=='audi')

print("cars[3]!='toyota', I predict true")
print(cars[3]!='toyota')

print("'jagaur' in cars, I predict false")
print('jaguar' in cars)

print("'range rover' not in cars, I predict true")
print('range rover' not in cars)

#diff ex
teams=['rcb','srh','rr','gt','lsg']
fixers=['csk','rr']
print("'rr' in teams and fixers, I predict True")
print('rr' in teams and 'rr' in teams)

print("csk in fixers and csk in team, I predict false")
print('csk' in fixers and'csk' in teams )

print("'csk' not in fixer or 'csk' in teams, I predict false")
print('csk' not in fixers or 'csk' in teams)

print("teams[0]=='rcb', I predict true")
print(teams[0]=='rcb')

print("'rcb' in fixers and 'rcb' in team, I predict false")
print('rcb' in fixers and 'rcb' in teams)

#numerical cinditions
abd=17
vk=18
print("\n",abd>vk,"predicted false")

print(abd==17,"true")
print(vk==17,"false")

car='Shelby'
print(car.lower()=='shelby',"true")

print('shelby' in car, 'false')

print(vk!=abd,'true')

print(car=='mazda','false')

print(abd!=28,'true')

print('bmw' in car,'false')

print(car in 'Shelby','true')

print(vk>18,'false')

print(abd<=17,'true')