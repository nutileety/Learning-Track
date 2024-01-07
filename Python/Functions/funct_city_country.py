def city_country(city_name,country_name):
    name_pairs = f'"{city_name}, {country_name}"'
    print(name_pairs)
    return name_pairs.title()
 
city_country('paris','londan')
city_country('bengaluru','india')
city_country('tokyo','japan')