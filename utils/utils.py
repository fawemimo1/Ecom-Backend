from geopy.geocoders import Nominatim
 
# Using Nominatim Api
zipcode1 = "756126"
zipcode2 = "756100"

try:
    geolocator = Nominatim(user_agent="jomodi")
    location1 = geolocator.geocode(zipcode1)
    location2 = geolocator.geocode(zipcode2)

    lat1 = location1.latitude
    lon1 = location1.longitude

    lat2 = location2.latitude
    lon2 = location2.longitude

    data = location1.raw
    loc_data = data['display_name'].split(",")
    dict = {'Area':loc_data[0], 'district':loc_data[1].replace('District',''),'state':loc_data[2], 
            'pincode':loc_data[3], 'country':loc_data[4]}
    print("Details of the Zipcode:", dict)
except Exception as e:
    print("Error is---->", str(e))

from datetime import timedelta,date
today = date.today()

from math import radians, cos, sin, asin, sqrt
def distance(lon1, lat1, lon2, lat2):       
    # radians which converts from degrees to radians. 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # Haversine formula  
    dlon = lon2 - lon1  
    dlat = lat2 - lat1 
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * asin(sqrt(a))  
    r = 6371 # Radius of earth in kilometers
    km_dis = int(c * r) # calculate the result 
    print('km_dis----->', km_dis)
    try:
        if km_dis < 50:
            d3 = date.today() + timedelta(days=1)
            return "delivery by Tomorrow, {day}".format(day=d3.strftime("%A"))
        elif km_dis < 100 & km_dis >= 50:
            d3 = date.today() + timedelta(days=2)
            return "delivery by {day}".format(day=d3.strftime("%d %b, %A"))
        elif km_dis < 300 & km_dis >= 100:
            d3 = date.today() + timedelta(days=3)
            return "delivery by {day}".format(day=d3.strftime("%d %b, %A"))
        elif km_dis <600 and km_dis >= 300:
            d3 = date.today() + timedelta(days=4)
            return "delivery by {day}".format(day=d3.strftime("%d %b, %A"))
        elif km_dis <1000 and km_dis >= 600:
            d3 = date.today() + timedelta(days=5)
            return "delivery by {day}".format(day=d3.strftime("%d %b, %A"))
        elif km_dis <1500 and km_dis >= 1000:
            d3 = date.today() + timedelta(days=6)
            return "delivery by {day}".format(day=d3.strftime("%d %b, %A"))
        elif km_dis <3000 and km_dis >=1500:
            d3 = date.today() + timedelta(days=7)
            return "delivery by {day}".format(day=d3.strftime("%d %b, %A"))
        else:
            return 'Order could not deliver for this address'
    except Exception as e:
        print("error is---->", e)


res = distance(lon1, lat1, lon2, lat2)
print('res is--->', res)


