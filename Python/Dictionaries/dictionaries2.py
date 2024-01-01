fav_lang={
    'ram':'c',
    'raj':'c++',
    'tom':'python',
    'john':'rust'
}

print(fav_lang.keys())
# using get() method
lang=fav_lang.get('tim','no tim')
print(lang)

print(fav_lang)
langauge = fav_lang['ram'].title()
print("The Ram's fav_lang is:",langauge)

for name,language in fav_lang.items():
    print(f"{name.title()} likes {language.title()} language very much")

for name in sorted(fav_lang): #or for name in fav_lang.keys:
    print(name.title())

print("\nThe used languages are :")
# The sets() used to remove repetations from dictionaries
for lang in set(fav_lang.values()): 
    print(lang.title())