import configparser
import io
import os
import requests
import search
import ast
import json
import re
import time
import load

#READ CONFIG.INI
config = configparser.ConfigParser()
with io.open("C:\Users\yn\Desktop\config.ini","r",encoding="utf-8") as f:
    config.optionxform = str
    config.read_file(f)

#AUTH
session = requests.Session()
session.auth = (str(config["API"]["key"]),"")


#ITEM TYPE
itemtype=[]
for key in config["ItemType"]:
   if config["ItemType"][key] == "yes":
        itemtype.append(str(key))

#PERMISSION FILTER
AssetTypeList=[]
FilterList = []
if config["PermissionFilter"]["visual"] == "yes":
   AssetTypeList.append("assets.visual:download")   
elif config["PermissionFilter"]["analytic"] == "yes":
   AssetTypeList.append("assets.analytic:download")


if len(AssetTypeList) != 0:
    permissionfilter = search.permission(AssetTypeList)
    FilterList.append(permissionfilter)


#GEOMETRY FILTER
if config["GeometryFilter"]["use"] == "yes":
   coordinates = config["GeometryFilter"]["coordinates"]
   clist = ast.literal_eval(coordinates)
   for i,row in enumerate(clist):
       for j,item in enumerate(row):
           clist[i][j] = (float(item))
   geometryfilter =search.geometry(config["GeometryFilter"]["shape"],[clist])
   FilterList.append(geometryfilter)
 
#DATE TIME FILTER 
if config["DateTimeFilter"]["use"] == "yes":
   datetimefilter = search.datetime(config["DateTimeFilter"]["start"],config["DateTimeFilter"]["end"])
   FilterList.append(datetimefilter)

#CLOUD COVER FILTER
if config["CloudCoverFilter"]["use"] == "yes":
   cloudcoverfilter = search.cloudcover(float(config["CloudCoverFilter"]["morethan"]),float(config["CloudCoverFilter"]["lessthan"]))
   FilterList.append(cloudcoverfilter)

#PIXEL RES FILTER
if config["PixelResFilter"]["use"] == "yes":
   pixelresfilter = search.pixelres(float(config["PixelResFilter"]["morethan"]),float(config["PixelResFilter"]["lessthan"]))
   FilterList.append(pixelresfilter)

#SEARCH BASED ON FILTERS
finalfilter = search.select_filters(FilterList)
request = search.endpoint_request(itemtype, finalfilter)
result = session.post("https://api.planet.com/data/v1/quick-search",json=request)
data = result.json()
#print data

#ACTIVATION AND DOWNLOAD           
directory = config["Download"]["FileDirectory"] 
load.activation(data,AssetTypeList,session,directory)


