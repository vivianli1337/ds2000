#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 13:51:21 2022

@author: vivian

weather
practicing with request library

go to long/lat https://bit.ly/ds2000weathers
go down https://bit.ly/ds2000sec2
"""
import requests

API_KEY = "459291d7a88e45e535150f4ede9bffad"


def main():
    func = "https://api.openweathermap.org/data/2.5/weather"
    params = {"lat" : 42.3371485, 
             "lon" : -71.091626, 
             "apiid" : API_KEY,
             "units" : "imperial"}
    response = requests.get(func, params)
    data = response.json()
    # see type of the data
    print(type(data))
    print(data)
    
    for key, value in data.items():
        print(key, "----", value)
        
    # see temperature
    #temp = data["main"]["temp"]
    #print(temp)
main()

