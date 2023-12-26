languages=['kannada','english','hindi','french']
languages[3]='sanskrit'
print("The modified list :",languages)

#adding new language
languages.append('telugu')
print("The appended list :",languages)

#inserting to the list
languages.insert(3,'tamil')
print("The inserted list :",languages)

#using "del" the element in the list
del languages[3]
print("the deleted list :",languages)

#using pop() to get deleted element from the list
poped_lang=languages.pop(4)
print("The poped list : {} and the poped element is '{}'".format(languages,poped_lang))

#using remove() to the to remove list value 
languages.remove("hindi")
print(languages[0].title())
print("The removed list :",languages)

#for sorting the list
print("This is temporary sorted list :",sorted(languages))
print("This is temporary reverse sorted list :",sorted(languages,reverse=True))
print(languages)
languages.sort()
print("This is permanent sorted list :",languages)
languages.sort(reverse=True)
print("This is permanent reversed list :",languages)

#New list is formed for reversing the unorganised list
cities=['bangaluru','hyderabad','kolkata','delhi']
cities.reverse()
print("The reversing the cities list :",cities)
print("The length of the languages :",len(languages))
print("The length of the cities :",len(cities))