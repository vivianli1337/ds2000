#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 14:01:16 2022

@author: vivian
"""

import matplotlib.pyplot as plt
def main():

    MEDAL_FILE = "us_medal_count.txt"

    # step one: gather US medal from file
    # file has one list per line
    # rn they are strings
    with open(MEDAL_FILE, "r") as infile:
        years = infile.readline()
        golds = infile.readline()
        silvers = infile.readline()
        bronze = infile.readline()
        
    # computation: modify/manipulate the list
    years = years.split(",")
    # rn they are using comma; use split to get rid of commas
    golds = golds.split(",")
    # its a string bc outcome has quotes
    silvers = silvers.split(",")
    bronze = bronze.split(",")
    
    #change from string to int
    for i in range(len(years)):
        years[i] = int(years[i])
        golds[i] = int(golds[i])
    
    for i in range(len(years)):
        print("In the", years[i], "US won:", golds[i], "gold metals")
    
    # plot list
    plt.scatter(years, golds, color = "gold")
    plt.show()
    plt.plot(golds)
    
    # step 3: communicate
    

main()