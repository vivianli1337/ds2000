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

def find_max_state(count_dct):
    """function find_max_state
    parameter: dictionary where key - string & 
        value - num (frequency/occurence tied to string)
    return: tuple of (key, value) of the key with the highest number
    """
    max_key = ""
    max_value = -1
    
    for key, value in count_dct.items():
        if value > max_value:
            max_value = value
            max_key = key
    return (max_key, max_value)
        

def main():
    # save dictionary
    # step 1: gather info from the file into a dictionary
    # states is the new dictionary
    states = csv_to_dict(NEU_FILE)
    
    max_state, max_students = find_max_state(states)
    print(max_state, "has the most student at Northeastern", max_students)
    
    # step 2 computation
    # figure out the number of people from a given state
    #state = input("What states?\n")
    #num_students = states[state]
    #print("There are", num_students, "students from", state + "!")
    
    # step 3 - iterate over dictionary and print the key, value pair
    #for key, value in states.items():    
        #print(key, "has", value, "students!")
    
                
main()
            