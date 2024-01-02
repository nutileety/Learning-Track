pizza={
    'crust':'thick',
    'toppings':['onion','extra cheese']
    }
print(f"The pizza with '{pizza['crust'].title()}' crust and witha the following toppings :")
for topping in pizza['toppings']:
    print("\t",topping.title())

# multiple fav lang
language={
    'ram':['python','rust'],
    'ravi':['c','c++'],
    'raj':['cobol','go'],
    'suri':['c']
     }
for name,lang in language.items():
    if len(lang) > 1:  
        print(f"{name.title()} like the following languages :")
        for langs in lang:
            print(langs.title())
    else:
        for langs in lang:
            print(f"{name.title()} has only one fav lang that is : {langs}")