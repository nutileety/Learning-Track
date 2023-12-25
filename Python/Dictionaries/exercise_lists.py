names=['dom','tom','john','jerry']
print(f"{names[0].title()}, please come to dinner")
print(f"{names[1].title()}, please come to dinner")
print(f"{names[2].title()}, please come to dinner")
print(f"{names[3].title()}, please come to dinner")

#tom can't make it to dinnerso inviting jack.
missed_guest=names.pop(1)
names.insert(1,'sona')
print(f"Sorry, {missed_guest.title()} can't make himself to dinner so I invited {names[1].title()} for dinner.")

#bigger table is avialable so have invite three more.
names.insert(0,'George')
names.insert(2,'Gina')
names.append('Borus')
print(names)

print("There is a shortage of tables for dinner so I can invite only two for the dinner")
remove_guests1=names.pop()
print("Sorry, I can't able to invite",remove_guests1.title())

remove_guests2=names.pop()
print("Sorry, I can't able to invite",remove_guests2.title())

remove_guests3=names.pop()
print("Sorry, I can't able to invite",remove_guests3.title())

remove_guests4=names.pop()
print("Sorry, I can't able to invite",remove_guests4.title())

remove_guests5=names.pop()
print("Sorry, I can't able to invite",remove_guests5.title())

print(f"{names[0].title()}, please come to dinner")
print(f"{names[1].title()}, please come to dinner")

del names[0]
del names[0]
print(names,"There is no person left")