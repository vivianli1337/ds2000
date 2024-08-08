#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 19:09:33 2022

@author: vivian

"""

import csv 
OLYMPICS = "athlete_events.csv"

def read_csv(filename):
    """ function: read csv
    paramter: filename, a string
    returns: 2d list of data in string
    
    """
    # open file & gather info into a list - full of given numbers
    data = []
    with open(filename, "r") as infile:
        csvfile = csv.reader(infile, delimiter = ",")
        for row in csvfile:
            data.append(row)
    return data

def main():
    # read file and put them inside a list
    data = []
    with open(OLYMPICS, "r") as infile:
        csvfile = csv.reader(infile, delimiter = ",")
        for row in csvfile:
            data.append(row)
        # create a new list with only the united states
        us_team = []
        # for every list in data; if "country" = united states
        for i in data:
            if i[6] == "United States":
                us_team.append(i)
        
        ten = []
        for i in us_team:
            if i[3] < "15":
                ten.append(i)
        gold = 0
        silver = 0
        bronze = 0
        na = 0
        for i in ten:
            if i[14] == "Gold":
                gold += 1
            elif i[14] == "Silver":
                silver += 1
            elif i[14] == "Bronze":
                bronze += 1
      
        print(gold)
        print(bronze)
        print(silver)
                
    
main()