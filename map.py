from geopy.geocoders import Nominatim
def locateHacker(city_address):
    g = Nominatim(user_agent="hacksmap")
    location = g.geocode(city_address)
    lst = [location.latitude, location.longitude]
    # lst.append(location.latitude)
    # lst.append(location.longitude)
    return lst
