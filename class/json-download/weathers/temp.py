'''
    temps.py
    DS2000
    Spring 2022
    
    Starter code for class on 4/15...
    
    There's nothing new in here, don't worry! Just reusing two functions
    we've done a lot recently: 
        1 - csv_to_dct, read a CSV file into a list of dictionaries
            (one dictionary per row in file, keys come from first row)
        2 - dct_to_weather, turn a list of dictionaries into objects
            (in this case, we're making Weather objects, but the function
             is basically the same as making Movie objects, and Review objects)
'''


import csv
from weather import Weather
import matplotlib.pyplot as plt

LOCATION = "Locations.csv"

def csv_to_dict(filename):
    ''' Function: csv_to_dict
        Parameter: filename, a string
        Returns: a list of dictionaries where each dictionary reps one row
                 of the file; keys of all dictionaries are file's first row
    '''
    data = []
    with open(filename, "r") as infile:
        csvfile = csv.reader(infile, delimiter = ",")
        keys = next(csvfile)
        for row in csvfile:
            d = {}
            for i in range(len(row)):
                d[keys[i]] = row[i]
            data.append(d)
    return data

def dct_to_weather(list_of_dct):
    ''' Function: dct_to_objs
        Parameters: list of dictionaries, where each one reps one location
        Returns: list of Weather objects
    '''
    weathers = []
    for d in list_of_dct:
        lat = float(d["latitude"])
        long = float(d["longitude"])
        w = Weather(lat, long)
        weathers.append(w)
    return weathers         

def main():
    # step 1: gather data from the file
    data = csv_to_dict(LOCATION)
    # step 2: turn list of dictionaries into objects
    weather = dct_to_weather(data)
    # step 3: communication: make the weather map
    lats = [w.lat for w in weather]
    longs = [w.long for w in weather]
    colors = [w.color for w in weather]
    
    plt.scatter(longs, lats, color = colors)
    
main()
    
