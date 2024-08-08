#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Vivian Shu Yi Li
    DS 2000
    Spring 2022
    HW1 - variables and operation
    January 27, 2021
    slugging.py
"""
"""
    test case #1
    0.86 target batting average
    2022: 508 hits to get that BA
    
    test case #2
    6.75 target batting average
    2022: 3989 hits to get that BA

"""
def main():
    # step 1 gathering info
    avg = float(input("What will the target batting average be in 2022?"))
    single = 89
    doubles = 37
    triples = 1
    HR = 38
    AB = 591
    c_hits = 165
    
    # step 2 computation
    
   
    TB = (single) + (2 * doubles) + (3 * triples) + (4 * HR)
    BA = c_hits / AB
    c_hits = single + doubles + triples + HR
    slugging = TB / AB
    r_hits = (avg * AB) - c_hits 
    hits = r_hits + c_hits
    
    
    # step 3 communication
    print("2021 results!\nHits:", c_hits)
    print("Total bases:", TB)
    print("Batting average:", round(BA,3))
    print("Slugging:", round(slugging,3))
    print("In 2022, Rafi Devers needs...Hits:", round(hits))
    print("To get BA:", avg)
    
    
main()