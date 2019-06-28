#Calling a JSON API
#url to use:   http://python-data.dr-chuck.net/geojson
#This API uses the same parameters (sensor and address) as the Google API.
#This API also has no rate limit so you can test as often as you like. 
#If you visit the URL with no parameters, you get a list of all of the address values which can be used with this API.
#To call the API, you need to provide a sensor=false parameter and the address that you are requesting as the address= parameter that is properly URL encoded using the urllib.urlencode() fuction as shown in http://www.pythonlearn.com/code/geojson.py

import urllib
import json

serviceurl = "http://python-data.dr-chuck.net/geojson?"

while True:

    address = raw_input("Enter location: ")

    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false','address':address})

    print 'Retrieving',url

    uh =urllib.urlopen(url)
    data = uh.read()
    print 'Retrived',len(data),'characters'

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
        continue

    placeid = js["results"][0]['place_id']
    print "Place id",placeid
