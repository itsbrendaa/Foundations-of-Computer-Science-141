print ("hi world")

print("11-1")

def city_country(city, country, population=None):
    """Return a neatly formatted city and country name, optionally with population."""
    if population:
        return f"{city.title()}, {country.title()} – population {population}"
    else:
        return f"{city.title()}, {country.title()}"
    
