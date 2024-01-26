def get_formated_name(firstname,lastname,middlename=''):
    if middlename:
        fullname = f"{firstname} {middlename} {lastname}"
    else:
        fullname = f"{firstname} {lastname}"
    return fullname.title()