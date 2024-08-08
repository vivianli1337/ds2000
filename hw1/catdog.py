#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Vivian Shu Yi Li
    DS 2000
    Spring 2022
    HW1 - variables and operation
    January 27, 2021
    catdog.py
"""
"""
    Test case #1
    60 kg = 132.00 lbs
    60 cm = 23.62 inches
    25 C = 77.00 F
    
    Test case #2
    26 kg = 57.20 lbs
    30 cm = 11.81 inches
    25 C = 77.00 F
    
    
    
"""

def main():
    # step 1 gather info
    name = input("What is your pet's name?\n")
    kg = float(input("What is its weight, in kg?\n"))
    cm = float(input("What is its length, in cm?\n"))
    C = float(input("What is its temperature in degrees celsium?\n"))
    
    # step 2 computation
    lbs = kg * 2.2
    inches = cm / 2.54
    F = C * 9/5 + 32
    
   #  step 3 communicate
    print("Converting from metric, here are", name + "''s stats: weight in kg:",\
          round(lbs,2), "length in inches:", round(inches,2), "temp in F:", round(F,2))
    
main()


