import ee
from ee.ee_exception import EEException
import time
import datetime


try:
    ee.Initialize()
except EEException as e:
    from oauth2client.service_account import ServiceAccountCredentials
    credentials = ServiceAccountCredentials.from_p12_keyfile(
    service_account_email='',
    filename='',
    private_key_password='notasecret',
    scopes=ee.oauth.SCOPE + ' https://www.googleapis.com/auth/drive ')
    ee.Initialize(credentials)

def ndvi(img):
    return img.expression('float(b("B4") - b("B3")) / (b("B4") + b("B3"))')

def executeNDVI(coords):
    geometry = ee.Geometry.Polygon(coords)
    collection = ee.ImageCollection('LANDSAT/LE07/C01/T1_TOA').filterDate('2002-11-01', '2018-08-01').filterBounds(geometry)
    vis = {'min': 0,'max': 1,'palette': 'FFFFFF,CE7E45,DF923D,F1B555,FCD163,99B718,74A901,66A000,529400,3E8601,207401,056201,004C00,023B01,012E01,011D01,011301'}
    ndvi_coll = collection.map(ndvi).mean()
    ndvi_map = ndvi_coll.getMapId(vis)

    mapid = ndvi_map['mapid']
    maptoken = ndvi_map['token']


    json_obj = {}

    json_obj["mapid"] = mapid
    json_obj["maptoken"] = maptoken

    return json_obj

