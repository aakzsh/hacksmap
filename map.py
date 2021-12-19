def locateHacker(city_address):
    from geopy.geocoders import Nominatim
    g = Nominatim(user_agent="hacksmap")
    location = g.geocode(city_address)
    return location.latitude,location.longitude