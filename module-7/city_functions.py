#Ryan Barber Assignment 7.2 2/22/26

def city_country(city, country, population=None, language=None):
    if population and language:
        return f"{city}, {country} - population {population}, {language}"
    elif population:
        return f"{city}, {country} - population {population}"
    else:
        return f"{city}, {country}"


print(city_country("Santiago", "Chile"))
print(city_country("Santiago", "Chile", 5000000))
print(city_country("Santiago", "Chile", 5000000, "Spanish"))
print(city_country("Paris", "France", 2000000))
print(city_country("Tokyo", "Japan", 1400000))