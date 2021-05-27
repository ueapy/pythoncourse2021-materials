
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


def create_sst(region_name):
    """
    Create fake SST data (degC) for a given region
    
    Inputs
    ------
    region_name: ...continue the docstring...
    
    n: integer, optional. Length of the returned data list      
    
    Returns
    -------
    ...continue the docstring...
    """
    
    if region_name == 'NS':
        # North Sea
        sst = list(range(5, 15, 1))
    elif region_name == 'WS':
        # White Sea
        sst = list(range(0, 10, 1))
    elif region_name == 'BS':
        # Black Sea
        sst = list(range(15, 25, 1))
    else:
        raise ValueError( f'Input value of {region_name} is not recognised')
        
    return sst
