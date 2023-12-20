str="Hi Nandeesh how are you"
char=input("enter char ")

if char in str:
    print("{0} is in the given string \"{1}\"".format(char,str))
else:
    print("{0} is not in the given stirng \"{1}\"".format(char,str))