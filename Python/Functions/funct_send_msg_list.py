def show_message(send_messages,sent_messages):
    print("The sending messages are: ")
    while send_messages:
        message = send_messages.pop()
        sent_messages.append(message)
        print(message.title())

def send_message(sent_messages):
    print("\nThe sent messages are:")
    for msg in sent_messages:
        print(msg.title())

send_messages = ['hi','hello','thank you','sorry']
sent_messages = []

show_message(send_messages[:],sent_messages)
send_message(sent_messages)

#Messages in list
print("\nThe sent messages are:",sent_messages)
print("The copy of sending messages are :",send_messages)