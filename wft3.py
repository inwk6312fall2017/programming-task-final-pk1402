#sucessfully installed weather api in the  pc
from weather import Weather
weather = Weather
#dummy=Weather
# Get weather forecasts for the upcoming days.

#for forecasts in location.forecast():
    #print forecasts['text']
    #print forecasts['date']
    #print forecasts['high']
    #print forecasts['low']
fc = location.forcast()[:5]
for forcast in fc:
	print(forcasts['text'])
	print(forcasts['date'])
	print(forcasts['high'])
	print(forcasts['low'])
def compute_stats(self):
	weather_handle = weather.Weather()
	self.high_temperature= []
	self.low_temperature=[]
	self.rainy_days_index=[]
	self.current_condition= ''
	location = self.weather_handle.lookup_by _location(self.metropolis)
	condition = location.condition()
	self.current_condition = condition['text']

	day_count = 0
	fc = location.forcasts()[:5]
