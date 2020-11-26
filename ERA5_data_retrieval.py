#!/usr/bin/env python

import numpy as np

## Previous - not sure if needed, as reference code ######
# from ecmwfapi import ECMWFDataServer
# server = ECMWFDataServer()
# server.retrieve({
# 	"class": "ea",
# 	"dataset": "era5",
# 	"date": date_before + "/to/" +date_after,
# # 		"date": '"'+date_before + "/to/" +date_after+'"',
# # 		"2012-04-09/to/2012-04-13",
# 	"expver": "1",
# 	"levelist": "1/2/3/5/7/10/20/30/50/70/100/125/150/175/200/225/250/300/350/400/450/500/550/600/650/700/750/775/800/825/850/875/900/925/950/975/1000",
# 	"levtype": "pl",
# 	"param": "130/131/132/133",
# 	"area": "74/-40/71/-36",
# 	"grid": "0.3/0.3",
# 	"stream": "oper",
# 	"time": "00:00:00/01:00:00/02:00:00/03:00:00/04:00:00/05:00:00/06:00:00/07:00:00/08:00:00/09:00:00/10:00:00/11:00:00/12:00:00/13:00:00/14:00:00/15:00:00/16:00:00/17:00:00/18:00:00/19:00:00/20:00:00/21:00:00/22:00:00/23:00:00",
# 	"type": "an",
# 	"target": "model_level_data/"+date[0:8]+"_levels",
# # 		"target": "20120411_state",
# 	"format": "netcdf",
# })


### This section can be used to download from the server... I think? Reference a working version above #####
# retrieve,
# class=ea,
# dataset=era5,
# date=2018-09-01/to/2018-09-30,
# expver=1,
# levtype=sfc,
# param=134.128/165.128/166.128/167.128/168.128,
# stream=oper,
# time=00:00:00/01:00:00/02:00:00/03:00:00/04:00:00/05:00:00/06:00:00/07:00:00/08:00:00/09:00:00/10:00:00/11:00:00/12:00:00/13:00:00/14:00:00/15:00:00/16:00:00/17:00:00/18:00:00/19:00:00/20:00:00/21:00:00/22:00:00/23:00:00,
# type=an,
# target="output"


#32.982675029015795, -96.75066793061926 #exact 
import cdsapi
c = cdsapi.Client()
c.retrieve('reanalysis-era5-complete', {
    'class': 'ea',
    'date': '2018-09-01/to/2018-09-30',
    'expver': '1',
    'levtype': 'sfc',
    'param': '134.128/165.128/166.128/167.128/168.128',
    'area': '33/-96.75',
#     'grid': '0.3/0.3'
    'stream': 'oper',
    'time': '00:00:00/01:00:00/02:00:00/03:00:00/04:00:00/05:00:00/06:00:00/07:00:00/08:00:00/09:00:00/10:00:00/11:00:00/12:00:00/13:00:00/14:00:00/15:00:00/16:00:00/17:00:00/18:00:00/19:00:00/20:00:00/21:00:00/22:00:00/23:00:00',
    'type': 'an',
    'format': 'netcdf',
}, 'UTD_sfc_data.nc')