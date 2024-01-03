fav_places={
    'maxi':['paris','londan','goa'],
    'faf':['italy','sweden','france'],
    'vk':['goa','german','switzerland']
    }
for name,list in fav_places.items():
    print(f"\n{name.title()}'s favorite places are :")
    for places in list:
        print("*",places.title())