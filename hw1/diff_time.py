#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Vivian Shu Yi Li
    DS 2000
    Spring 2022
    HW1 - variables and operation
    January 27, 2021
    time.py
"""
"""
    Test case #1
    Current: Day 3 Hour 5
    Leap: 7 hours
    It will be: Day 3 Hour 12
    
    Test case #2
    Current: Day 4 Hour 9
    Leap: 358 hours
    It will be: Day 19 Hour 7

"""

def main():
    # step 1 gather info
    current_day = int(input("What day is today?"))
    current_hour = int(input("What hour is it right now?"))
    leap_hour = int(input("How many hours into the future is Sam going on his next leap?"))
    
    # step 2 computation
    future_hour = (current_hour +  leap_hour)%24
    future_day = current_day + (current_hour + leap_hour)//24
    
    
    
    # step 3 communication
    print("It is currently Day", current_day, ",hour", current_hour)
    print("Sam will leap to Day", future_day)
    print("And he will lep to Hour", future_hour)
   
    
main()
