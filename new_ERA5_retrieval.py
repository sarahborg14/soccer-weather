import cdsapi
c = cdsapi.Client()
c.retrieve('reanalysis-era5-complete', 
	{
    'class': 'ea',
    'date': '2018-09-01/2018-09-30/', #I think I can connect dates in this way? 
    'expver': '1',
    'levtype': 'sfc',
    'param': '134.128/165.128/166.128/167.128/168.128',
    'area': '33/-96.75',
#     'grid': '0.3/0.3'
    'stream': 'oper',
    'time': '00:00:00/01:00:00/02:00:00/03:00:00/04:00:00/05:00:00/06:00:00/07:00:00/08:00:00/09:00:00/10:00:00/11:00:00/12:00:00/13:00:00/14:00:00/15:00:00/16:00:00/17:00:00/18:00:00/19:00:00/20:00:00/21:00:00/22:00:00/23:00:00',
    'type': 'an',
    'target': 'sfc_data.nc',
    'format': 'netcdf'
    },
)