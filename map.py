def locateHacker(city_address):
    from geopy.geocoders import Nominatim
    g = Nominatim(user_agent="hacksmap")
    location = g.geocode(city_address)
    lst = []
    lst.append(location.latitude)
    lst.append(location.longitude)
    return lst
