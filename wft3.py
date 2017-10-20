#sucessfully installed weather api in the  pc
from weather import Weather
weather = Weather
dummy=Weather

#Lookup WOEID via http://weather.yahoo.com.

#lookup = weather.lookup(560743)
#condition = lookup.condition()
#print ['condition']

# Lookup via location name.

location = weather.lookup_by_location('halifax')
condition = location.condition()
#print ['condition']

# Get weather forecasts for the upcoming days.

#for forecasts in location.forecast():
    #print forecasts['text']
    #print forecasts['date']
    #print forecasts['high']
    #print forecasts['low']
