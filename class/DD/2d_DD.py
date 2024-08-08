#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 14:20:41 2022

@author: vivian
"""


DD_FILE = "DD_US.csv"
LANEY_LAT = 42.30537
LANEY_LONG = -71.061
LAT_COL = 1
LONG_COL = 0
ADDRESS_COL = 2

import csv
import matplotlib.pyplot as plt

def euclidean(x1, y1, x2, y2):
    """ fuction euclidean
    paramenter: four floats, representing two points in the x/y plane
    returns = float, the euclidean distance vetween the points
    """
    x_diff = (x2-x1)**2
    y_diff = (y2-y1)**2
    distance = x_diff + y_diff
    distance = distance ** 0.5
    return distance
    
def get_lat_long(dd_row, lat_col, long_col):
    """ fuction get_lat_long
    parameter" a strong, one line from the DD CSV file
    return: a list of two floats - the lat/long of a DD location
    """
    dd = dd_row.split(",")
    lat = float(dd[lat_col])
    long = float(dd[long_col])
    lst = [lat, long]
    return lst
    

def read_csv(filename):
    """function read_csv
    parameter: filename to read (string)
    returns: 2d list of strings, the contents of the file
    """
    # comma separated value = csv
    data = []
    with open(filename, "r") as infile:
        csvfile = csv.reader(infile, delimiter = ",")
        
        for row in csvfile:
            data.append(row)
            
    return data
            
def get_local(dd, city, col):
    """function get_local
    parameters: 2d listt of strings, a city to look for,
        and a column number where to find the city
    returns: a 2d list, similar to the first list, but ONLY
        with city matches
    """
    city_only = []
    #iterate over 2d
    for row in dd:
        if city in row[col]:
            city_only.append(row)
    return city_only
    
    
def main():
    # step 1: gather data from the file, into a 2d list
    data = read_csv(DD_FILE)
    
    # step 2: computation! final all the dd's in the city we're
    # looking for
    city = input("Enter a city to find Dunks!\n")
    local = get_local(data, city, ADDRESS_COL)
    
    #step 3: communicate! report all the DDs in the city
    print(local)
    

    
    
main()   
    