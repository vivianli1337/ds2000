#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 13:24:10 2022

@author: vivian
"""

DD_FILE = "DD_US.csv"
LAT_COL = 1
LONG_COL = 0

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
    
    
def main():
    laney_lat = 42.30537
    laney_long = -71.851
    lats = []
    longs =[]
    
    with open (DD_FILE, "r") as infile:
        header = infile.readline()
        
        while True:
            dd = infile.readline()
            if dd == "":
                break
            
            
            
            
            # step 2 computation
            
            """
            dd = dd.split(",")
            lat = float(dd[LAT_COL])
            long = float(dd[LONG_COL])
            """
            coords = get_lat_long(dd, LAT_COL, LONG_COL)
            dist = euclidean(laney_lat, laney_long, coords[0], coords[1])
            
            print("Distance to my house to dunkins", dist)
            lats.append(coords[0])
            longs.append(coords[1])
            
    
  # step 3 plot
    plt.scatter(longs, lats, color = "orange")
    plt.plot(laney_long, laney_lat, color = "mint")
    
    
    
main()