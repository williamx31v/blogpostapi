#!/usr/bin/python
# -*- coding: utf-8 -*-

#define modules for import

import psycopg2
import sys
import cgi
import html
import pprint
import psycopg2.extras
import requests
import json

#Set our variables

formData = cgi.FieldStorage()
address = formData.getvalue('address')
city = formData.getvalue('city')
state = formData.getvalue('state')
zip_code = formData.getvalue('zip_code')
column_names = []
data_rows = []
address_r = address.replace(" ", "+")

url = 'https://geocoding.geo.census.gov/geocoder/locations/address?'

req_url = url+'street='+address_r+'&city='+city+'&state='+state+'&zip='+zip_code+'&benchmark=Public_AR_Current&format=json'

r = requests.get(req_url)
data = r.json()
data_1 = data['result']['addressMatches']
coords = data_1[0]['coordinates']
lat = coords['y']
lon = coords['x']

print "Content-Type: text/html"
print ""
print "<p>"
print "Address:<b> %s.</b><br/>" %(address) 
print "City:<b> %s </b><br/>" %(city)
print "State:<b> %s </b><br/>" %(state)
print "Zip:<b> %s </b><br/>" %(zip_code)
print "Encoded Address:<b> %s </b><br/>" %(address_r)
print "URL:<b> %s </b><br/>" %(url)
print "Request URL:<b> %s <b/><br/>" %(req_url)
print "Lattitude:<b> %s <b/><br/>" %(lat)
print "Longitude:<b> %s <b/><br/>" %(lon)
print "</p>"

#Connect to the database
con = None

try:
     
     con = psycopg2.connect(dbname='test', user='postgres', host= '192.168.56.101', password= 'postgres')
except:
     print "Content-Type: text/html"
     print ""
     print "I can't connect to the database!"

#Do some inserts 

cur = con.cursor()
cur.execute("INSERT INTO address_lat_long VALUES (%s, %s, %s, %s, %s, %s)", (address, city, state, zip_code, lat, lon))
con.commit()
con.close()

print """<form method="post" action="http://192.168.56.101/geo-code.htm">
<button type="submit">Back to Contact Page</button>
</form>"""