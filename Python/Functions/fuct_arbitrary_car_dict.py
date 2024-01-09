def car_info(company,model,**cars_details):
    cars = { 
           'company': company,
           'model':model
           }
    # print("The car and its info :")
    for key,value in cars_details.items():
        cars[key] = value
        
    return cars

output = car_info('bmw','m4 coupe',color = 'Black',open_top = 'Yes')
print(output)
