fav_number = {
    'Ben':5,
    'George':3,
    'David':8,
    'Charlie':9,
    'Sam':4
}

print("Favorite number are :",fav_number)

if fav_number['Ben'] > 5:
    fav_number['Ben']=fav_number['Ben'] + 1
    fav_number['George']=fav_number['George'] + 1
    fav_number['David']=fav_number['David'] + 1
    fav_number['Charlie']=fav_number['Charlie'] + 1
    fav_number['Sam']=fav_number['Sam'] + 1
    print("The modified vlaue :\n",fav_number)
if fav_number['Ben'] < 5:
    fav_number['Ben']=fav_number['Ben'] - 1
    fav_number['George']=fav_number['George'] - 1
    fav_number['David']=fav_number['David'] - 1
    fav_number['Charlie']=fav_number['Charlie'] - 1
    fav_number['Sam']=fav_number['Sam'] - 1
    print("The modified vlaue :\n",fav_number)
else:
    fav_number['Ben']=fav_number['Ben']
    fav_number['George']=fav_number['George']
    fav_number['David']=fav_number['David']
    fav_number['Charlie']=fav_number['Charlie']
    fav_number['Sam']=fav_number['Sam']
    print("No changes in the dictionary!")
    
print("Finished!")