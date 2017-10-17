names = ['Julian', 'Zach', 'Alex']
scores = [95, 75, 85]

grades = dict()

print(grades)

grades['Zach'] = 75 #Key value pair

print(grades)

print(grades['Zach'])

grades = {'Zach': 75, 'Alex': 85, 'Julian': 95}

print(grades)

grades['Xiang'] = 88

print(grades)

print(len(grades))

print('Zach' in grades)
print('Zhi' in grades)

def histogram(s):
    d = dict()
    for c in s.lower():
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

h = histogram('Bookbookkeeper')
print(histogram('Bookbookkeeper'))

number_of_e = h.get('e', 0)
number_of_a = h.get('a', 0)
print(number_of_e)
print(number_of_a)

def histogram1(s):
    d = dict()
    for c in s.lower():
        d[c]= d.get(c, 0) + 1
    return d

h1 = histogram1('Bookbookkeeper')
print(h1)

def print_hist(h):
    for c in h:
        print(c, h[c])

h3 = histogram('Massachusetts')
print_hist(h3)

for key in sorted(h3):
    print(key, h3[key])

json_example = {
   "results" : [
      {
         "address_components" : [
            {
               "long_name" : "231",
               "short_name" : "231",
               "types" : [ "street_number" ]
            },
            {
               "long_name" : "Forest Street",
               "short_name" : "Forest St",
               "types" : [ "route" ]
            },
            {
               "long_name" : "Babson Park",
               "short_name" : "Babson Park",
               "types" : [ "neighborhood", "political" ]
            },
            {
               "long_name" : "Wellesley",
               "short_name" : "Wellesley",
               "types" : [ "locality", "political" ]
            },
            {
               "long_name" : "Norfolk County",
               "short_name" : "Norfolk County",
               "types" : [ "administrative_area_level_2", "political" ]
            },
            {
               "long_name" : "Massachusetts",
               "short_name" : "MA",
               "types" : [ "administrative_area_level_1", "political" ]
            },
            {
               "long_name" : "United States",
               "short_name" : "US",
               "types" : [ "country", "political" ]
            },
            {
               "long_name" : "02457",
               "short_name" : "02457",
               "types" : [ "postal_code" ]
            },
            {
               "long_name" : "0310",
               "short_name" : "0310",
               "types" : [ "postal_code_suffix" ]
            }
         ],
         "formatted_address" : "231 Forest St, Babson Park, MA 02457, USA",
         "geometry" : {
            "location" : {
               "lat" : 42.2993708,
               "lng" : -71.2659951
            },
            "location_type" : "ROOFTOP",
            "viewport" : {
               "northeast" : {
                  "lat" : 42.3007197802915,
                  "lng" : -71.26464611970849
               },
               "southwest" : {
                  "lat" : 42.2980218197085,
                  "lng" : -71.26734408029149
               }
            }
         },
         "place_id" : "ChIJ7xQZi0GB44kRiWrnmTgf904",
         "types" : [ "establishment", "point_of_interest" ]
      }
   ],
   "status" : "OK"
}

import json
import urllib2
json_example1 = json.load(urllib2.urlopen("https://maps.googleapis.com/maps/api/geocode/json?address=Babson+College"))

print(json_example1)