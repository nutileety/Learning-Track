responses = {}
while True:
    name = input("What's your name? ")
    response = input("which country you to wist in your in your life time:")
    
    #add name and reponse to the dictionary
    responses[name] = response

    repeat = input("want to enter another response enter(yes/no): ")
    if repeat == 'no':
        break

for name,response in responses.items():
    print(f"{name.title()} want to visit {response.title()} in his/her life time.")

print("Thank you for your time!")