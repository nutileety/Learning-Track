from city_function import city_names

def test_city_country():
    correct = city_names('paris','londan')
    assert correct == 'Paris, Londan'

def test_city_country_population():
    correct = city_names('paris','londan','5000000')
    assert correct == 'Paris, Londan, Population-5000000'