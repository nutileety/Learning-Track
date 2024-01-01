fav_lang={
    'ram': 'c',
    'raj': 'c++',
    'tom': 'python', 
    'john': 'rust'
    }
friends=['ram','raj']
for name in fav_lang.keys():
    print(name.title())

    if name in friends:
        print(f"{name.title()}'s favarite language is : {fav_lang[name].title()}")

    if 'ben' not in fav_lang:
        print("Ben, Is not in the poll\n")

#if the elements inside braces does not have keys and value pairs,
# then that is said to be a "set"

set_lang={'pyhton','c++','c','python'}
print("this is a only set: \n",set_lang)