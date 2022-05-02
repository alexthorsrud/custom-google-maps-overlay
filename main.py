import googlemaps
import gmplot

import argparse

apikey="SET YOUR API KEY HERE"

#arg parsing
parser = argparse.ArgumentParser(description='Map maker.')
parser.add_argument('-k', default=apikey)
parser.add_argument('-c', nargs=2)
parser.add_argument('-z', nargs=1, default=11)
args = parser.parse_args()

#google maps api and map rendering
google_maps = googlemaps.Client(key=apikey)
gmap = gmplot.GoogleMapPlotter(args.c[0], args.c[1], args.z, apikey=apikey)

#target
#get locations
target_locations = google_maps.places("target", args.c, 1000)
target_lats = [] 
target_longs = []
#get lat and long from each result
for item in target_locations['results']:
    target_lats.append(item['geometry']['location']['lat'])
    target_longs.append(item['geometry']['location']['lng'])

#plot targets
gmap.scatter(target_lats, target_longs, color='#FF0000', size=804.5, marker=False)

#kroger
kroger_locations = google_maps.places("kroger", args.c, 1000)
kroger_lats = []
kroger_longs = []
for item in kroger_locations['results']:
    kroger_lats.append(item['geometry']['location']['lat'])
    kroger_longs.append(item['geometry']['location']['lng'])

gmap.scatter(kroger_lats, kroger_longs, color='#0067B2', size=804.5, marker=False)

#publix
publix_locations = google_maps.places("publix", args.c, 1000)
publix_lats = []
publix_longs = []
for item in publix_locations['results']:
    publix_lats.append(item['geometry']['location']['lat'])
    publix_longs.append(item['geometry']['location']['lng'])

gmap.scatter(publix_lats, publix_longs, color='#4C9A42', size=804.5, marker=False)

# Draw the map to an HTML file:
gmap.draw('map.html')