def formatted_name(firstname,lastname):
    fullname = f"{firstname} {lastname}"
    return fullname.title()

name = formatted_name('john','wick')
print(name)