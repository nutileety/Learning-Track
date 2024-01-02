pets_info = []
pet = {
    'pet':'cat',
    'pet_name':'tommy',
    'pet_owner':'jordan'
    }
pets_info.append(pet)
pet = {
    'pet':'dog',
    'pet_name':'dolly',
    'pet_owner':'john'
    }
pets_info.append(pet)
pet = {
    'pet':'parrot',
    'pet_name':'honey',
    'pet_owner':'joy'
    }
pets_info.append(pet)

print("The pet information :")
for pet in pets_info:
    print(f"\nThe info of pet : {pet['pet_name']}")
    for key,value in pet.items():
        print(f"\t{key} : {value}")






    # pet=pet_info['pet'].title()
    # owner=pet_info['pet_owner'].title()

    # print("Type of pet :",pet)
    # print("Name of the pet owner :",owner,"\n")