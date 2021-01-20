import cdsapi
import numpy as np

def ERA5_data_retrieval(date_list, coords, output_path): 
    # date_list must be string in format '2020-09-31/2020-10-20', 
            # Keep in mind, only dates up to 3 months prior to current are available 
    # output_path must be string in format 'filename.nc' for netcdf 
    # will add arguments for other parameters later
    cds = cdsapi.Client()
    cds.retrieve('reanalysis-era5-complete', 
    {
    'class': 'ea',
#     'date': '2020-09-20/2020-10-03/2020-10-17',
#         /2020-11-07/2020-11-29/2020-12-05/2020-12-21/2020-12-28/2021-01-03', 
    'date': date_list, 
    'expver': '1',
    'levtype': 'sfc',
    'param': '134.128/165.128/166.128/167.128/168.128',
#     "area": "32.5/-97/33/-96.5",
    "area": coords,
    "grid": "0.25/0.25",
    'stream': 'oper',
    'time': '00:00:00/01:00:00/02:00:00/03:00:00/04:00:00/05:00:00/06:00:00/07:00:00/08:00:00/09:00:00/10:00:00/11:00:00/12:00:00/13:00:00/14:00:00/15:00:00/16:00:00/17:00:00/18:00:00/19:00:00/20:00:00/21:00:00/22:00:00/23:00:00',
    'type': 'an',
    'format': 'netcdf',   
    }, output_path)
    

    
def find_nearest(array, value):
    #Returns index of nearest value
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx