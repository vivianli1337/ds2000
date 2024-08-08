'''
    weather.py
    DS2000
    Spring 2022
    
    Starter code for class on 4/15...
    
    Starting out a Weather ojbect. It has lat/long attributes, so we're talking
    about the weather at a specific location. What we want to figure out
    is the temperature at that specific location.
    
    Since we want to figure out the current temp, using a CSV file would
    be pretty silly! It'd never get updated quickly enough, and it would have
    to be huge to cover every lat/long location in the US. 
    
    So what's a better fit, if available? An API! In class we'll add in 
    the part still needed below, getting the current temp at this
    location by calling an API function.
'''

import requests
API_KEY = "459291d7a88e45e535150f4ede9bffad"

class Weather:
    def __init__(self, lat, long, api_key = API_KEY):
        ''' create a weather object with the given latitude and longitude'''
        self.lat = lat
        self.long = long
        self.api_key = api_key
        self.temp = 291
        self.set_temp()
        self.color = "red"
        self.set_color()
        
        
    def set_temp(self):
        """ set the current temp for the lat/long"""
        func = "https://api.openweathermap.org/data/2.5/weather"
        params = {"lat" : 42.3371485, 
                 "lon" : -71.091626, 
                 "apiid" : API_KEY,
                 "units" : "imperial"}
        response = requests.get(func, params)
        data = response.json()
        self.temp = data["main"]["temp"]
        
    
    def set_color(self):
        """ set the color that goes with the temp """
        if self.temp < 0:
            self.color = "mediumslateblue"
        elif self.temp < 32:
            self.color = "mediumblue"
        elif self.temp < 50:
            self.color = "cyan"
        elif self.temp < 60:
            self.color = "lightgreen"
        elif self.temp < 68:
            self.color = "lightsalmon"
        elif self.temp < 75:
            self.color = "salmon"
        elif self.temp < 85:
            self.color = "red"
        else:
            self.color = "darkred"
        
    

