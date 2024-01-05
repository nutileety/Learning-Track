number = 1
while number <= 5:
    print(number)
    number += 1

    # Repeating the while loop unitl user enters the quit msg
prompt = "These will repeat the message unitl the you enters the 'quit' msg"
msg=""
while msg != 'quit':
    msg = input("enter something :")
    # print(f"{msg}") #used with 'if' when quit will print and exit
    if msg != 'quit':
      print(f"{msg}")
