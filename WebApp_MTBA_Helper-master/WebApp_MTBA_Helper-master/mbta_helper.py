import urllib.request   # urlencode function
import urllib.parse
import json
from pprint import pprint
import requests

# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json?address=#streetAddress,+#city,+#abrState&key=AIzaSyBVZhQwm7GZViRzTCuH1VBvMdIpLMwvfT4"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation?api_key=wX9NwuHnZU2ToO7GmGR9uw&lat=#latitude&lon=#longitude&format=json"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"

# A little bit of scaffolding if you want to use it

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    pprint(response_data)


def get_lat_long(address):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {'address':address,'key':'AIzaSyBVZhQwm7GZViRzTCuH1VBvMdIpLMwvfT4'}
    req = requests.get(url,params=params)
    stat = req.status_code
    latitude = req.json()['results'][0]['geometry']['location']['lat']
    longitude = req.json()['results'][0]['geometry']['location']['lng']
    return latitude, longitude

     


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.
    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API in 'MBTA-realtime API v2 Documentation'.
    """
    url1 = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
    params1 = {'api_key':'lm1M_mXgq0O6dsH9xduPAQ','lat':latitude,'lon':longitude,'format':'json'}
    req1 = requests.get(url1,params=params1)
    stat1 = req1.status_code
    stop_name = req1.json()['stop'][0]['stop_name']
    distance = req1.json()['stop'][0]['distance']
    return stop_name, distance


    


def find_stop_near(address):
    """
    Given a place name or address, return the nearest MBTA stop and the 
    distance from the given place to that stop.
    """
    latlong = get_lat_long(address)
    latitude = latlong[0]
    longitude = latlong[1]
    nearStop = get_nearest_station(latitude, longitude)
    return nearStop


    

def main():
    #print(get_json(GMAPS_BASE_URL))
    address = input('please enter a place or an address: ')
    print('The Latitude and Longitude are:', get_lat_long(address))
    # print(latlong)
    # print(latitude)
    # print(longitude)
    # latitudeInput = float(input('please enter a latitude: '))
    # longitudeInput = float(input('please enter a longitude: '))
    print('The closest station to this location and the distance (miles) away are:', find_stop_near(address))
    

if __name__ == '__main__':
    main()

