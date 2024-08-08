#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
  Vivian Shu Yi Li
  DS 2000
  Spring 2022
  HW4
  February 25, 2021
  running.py
"""
def main():
   
    RUNNER_FILE = "runner_data.txt"
    import matplotlib.pyplot as plt

    all_name = []
    miles = []
    all_day = []
  
    # step 1: gather info from file 
    with open (RUNNER_FILE, "r") as infile:
        january = infile.readline()
        
        # use a while loop to calculate information of each runner
        while True:
            runner = infile.readline()
            if runner == "":
                break
           
            # step 2 computation - calculate the days
            # make a list of strings so we can slice the data 
            runner = runner.split()
            name = runner[0] + " " + runner[1]
            all_name.append(name)
            miles = [float(x) for x in runner[2:]]
            
            # day = 0 is used to reset the days after each runner
            day = 0
            for i in miles:
                if i >= 1:
                    day += 1
            all_day.append(day)
        
        # use "max" to find runner with the highest number of days
        # credit to TA Devarsh Hemantbhai Patel for helping with max_runner 
        # code organization
        max_runner = all_name[all_day.index(max(all_day))]  
        max_day = max(all_day)
        
        # step 3 communication
        print(max_runner, "has the highest number of running days (", max_day,
              ") days in January")
        
    # create a bar graph
    color = ["pink", "palegreen", "plum", "skyblue"]
    plt.bar(all_name, all_day, color = color)
    plt.title("Running Days")
    plt.ylabel("Number of Days")
    plt.xlabel("Runners")
    plt.ylim(0, 31) 
                        
    
main()