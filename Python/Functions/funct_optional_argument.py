def formatted_name(firstname,lastname,middlename=''):
    if middlename:
        fullname = f"{firstname} {middlename} {lastname}"
    else:
        fullname = f"{firstname} {lastname}"
    return fullname.title()

output = formatted_name('john','dwane','junior')
print(output)
output2 = formatted_name('john','wick')
print(output2)

#optional parameter in the dictionary
def details(firstname,lastname,age=None):
    fullname = {'first':firstname,'last':lastname}
    if age:
        fullname['age'] = age
    return fullname

output = details('john','wick',27)
print(output)