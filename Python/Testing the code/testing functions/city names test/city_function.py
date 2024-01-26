def city_names(city,country,population=''):
    if population:
        place = f"{city}, {country}, Population-{population}"
    else:
        place = f"{city}, {country}"    
    return place.title()