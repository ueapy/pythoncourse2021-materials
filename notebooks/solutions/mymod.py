
def calc_heat_flux(
    u_atm, 
    t_sea, 
    rho=1.2, 
    c_p=1004.5, 
    c_h=1.2e-3, 
    u_sea=1, 
    t_atm=17):

    # Calculates bulk heat flux from sea surface
    q = rho * c_p * c_h * (u_atm - u_sea) * (t_sea - t_atm)
    
    return q



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
