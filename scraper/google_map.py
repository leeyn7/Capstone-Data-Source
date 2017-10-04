from PIL import Image
from io import StringIO
import urllib.request
import os
import math

class GoogleMapScrapper:

    def __init__(self, lat, lng, zoom=18, api_key='AIzaSyD7atkiOxRi2B0nqg2VOkcFmgOefC_N7TU'):
        self._lat = lat
        self._lng = lng
        self._zoom = zoom
        self._api_key = api_key

    def generateImage(self):
        request = 'https://maps.googleapis.com/maps/api/staticmap?maptype=satellite&center=' + str(self._lat) + ',' + str(self._lng) + '&zoom=' + str(self._zoom) + '&size=640x400&key=' + str(self._api_key)
        urllib.request.urlretrieve(request, str(self._lat) + "_" + str(self._lng) + ".png")

def main():

    latitude = 1.3403
    longitude = 103.9629

    gms = GoogleMapScrapper(latitude, longitude)

    try:
        gms.generateImage()
    except IOError:
        print("Could not generate the image - try adjusting the zoom level and checking your coordinates")
    else:
        print("The map has successfully been saved")


if __name__ == '__main__':
    main()
