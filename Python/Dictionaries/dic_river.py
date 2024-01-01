rivers={
    'nile':'africa',
    'ganges':'india',
    'amazon':'peru'
    }
for river,country in rivers.items():
    print(f"{river.title()} run through {country.title()}.")

print("\nThe list of rivers:")
for river in rivers.keys():
    print(river.title())

print("\nThe list of country :")
for country in rivers.values():
    print(country.title())