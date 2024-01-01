fav_lang={
    'ram': 'c', 
    'raj': 'c++', 
    'tom': 'python', 
    'john': 'rust'
    }
people=['ram','tim','george','john']
for name in people:
    if name in fav_lang.keys():
        print(f"Hello {name.title()}, you are already in the poll")
    else:
        print(f"Hello {name.title()}, You are invited to our poll")