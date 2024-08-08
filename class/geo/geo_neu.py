#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 14:02:27 2022

@author: vivian
"""
import csv

NEU_FILE = "neu_geo.csv"

def csv_to_dict(filename):
    """function csv_to_dict
    parameter: name of the scv file, a string
    return: dictionary where key - state (str),
    value - # of students for that state (int)
    """
    
    data = {}
    with open(filename, "r") as infile:
        csvfile = csv.reader(infile, delimiter = ",")
        next(csvfile)
        # next- skip the header
        for row in csvfile:
            data[row[0]] = int(row[1])
            # no need for split bc of csv
    return data

def main():
    # save dictionary
    # step 1: gather info from the file into a dictionary
    # states is the new dictionary
    states = csv_to_dict(NEU_FILE)
    print(states)
    
    # step 2 computation
    # figure out the number of people from a given state
    state = input("What states?\n")
    num_students = states[state]
    print("There are", num_students, "students from", state + "!")
    
    # step 3 - iterate over dictionary and print the key, value pair
    for key, value in states.items():    
        print(key, "has", value, "students!")
    
                
main()
            