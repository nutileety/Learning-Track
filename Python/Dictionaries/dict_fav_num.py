fav_number={
    'brain':[4,34,54],
    'dom':[7,77,777],
    'shaw':[8,83,38],
    'roman':[55,64,44],
    'tej':[66,75,55]
    }
for name,num_list in fav_number.items():
    print(f"\n{name}'s favarite numbers are :")
    for number in num_list:
        print("-",number) 