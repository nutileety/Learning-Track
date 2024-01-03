cities={
    'bangaluru':{
        'population':8_443_000,
        'fact':'silicon chips',
        'country':'india'
        },
    'paris':{
        'population':2_148_000,
        'fact':'eiffel tower',
        'country':'france'
        },
    'london':{
        'population':8_825_000,
        'fact':'big ben clock tower',
        'country':'united kingdom'
        }
    }
for city,info in cities.items():
    print(f"\n{city.title()}'s info :")
    for key,value in info.items():
        print(f"* {key.title()} : {str(value).title()}")