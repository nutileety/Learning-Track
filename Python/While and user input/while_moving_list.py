unconfirmed_user=['ram','raj','john']
confirmed_user=[]

while unconfirmed_user:
    current_user=unconfirmed_user.pop()
    print("The verifying users:",current_user.title())
    confirmed_user.append(current_user)

print(f"\nThe verified users are:")
for verified in confirmed_user:
    print(verified.title())