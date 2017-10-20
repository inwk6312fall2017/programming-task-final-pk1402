#sucessfully installed weather api in the  pc
from weather import Weather
weather = Weather
dummy=Weather
# Get weather forecasts for the upcoming days.

#for forecasts in location.forecast():
    #print forecasts['text']
    #print forecasts['date']
    #print forecasts['high']
    #print forecasts['low']
forecastslist = location.forcast()[:5]
for forcast in forecastslist:
	print(forcasts['text'])
	print(forcasts['date'])
	print(forcasts['high'])
	print(forcasts['low'])
