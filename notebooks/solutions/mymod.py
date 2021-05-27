import requests
import urllib.parse
from math import cos, sin, acos, pi


def calc_co2e(dist,
              returnf=False,
              firstclass=False,
              radforc=2.0,
              ):
    """
    calculate equivalent carbon emissions from flights
    
    Parameters
    ==========
    dist - flight distance in km
    
    Optional inputs
    ---------------
    returnf - Return flight (default=False)
    firstclass - First class flight (default=False)
    radforc - radiative forcing factor (default=2.0)
    
    Returns
    =======
    CO2 equivalent emissions in kg

    Emission factors (kg CO2e/pkm)
    https://flygrn.com/blog/carbon-emission-factors-used-by-flygrn
    
    0.26744  < 700 km 
    0.15845  700 – 2500
    0.15119  > 2500 km 
    """

    if dist < 700:
        emm_factor = 0.26744
    elif dist > 2500:
        emm_factor = 0.15119
    else:
        emm_factor = 0.15845
        
    co2e = emm_factor * dist

    if returnf:
        co2e = co2e * 2
    if firstclass:
        co2e = co2e * 2
    
    co2e = co2e / 2.0 * radforc
    
    return co2e


def calc_dist(origin, destination):
    """
    Calculate distances for a given itenerary
    
    Inputs
    ------
    origin, destination - names of the cities
        
    Returns
    -------
    distance in km
    
    Uses:
    Great circle approximation for spherical earth
    dist = 6378.388 * acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon2 - lon1))
    where lat and lon are in radians
    """

    (lat1,lon1) = get_latlon(origin)
    (lat2,lon2) = get_latlon(destination)
    lat1 = lat1/180*pi
    lon1 = lon1/180*pi
    lat2 = lat2/180*pi
    lon2 = lon2/180*pi
    
    dist = 6378.388 * acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon2 - lon1))
        
    return dist


def get_latlon(location):
    
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(location) +'?format=json'

    response = requests.get(url).json()

    if not response:
        print('Location not found:',location)
    
    lat = float( response[0]["lat"] )
    lon = float( response[0]["lon"] )
    
    return (lat,lon)