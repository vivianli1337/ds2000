#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 13:50:10 2022

@author: vivian
"""

"""
miles vs speed
heartbeat vs speed
time vs miles
step vs miles

scatterplot/line plot
day vs steps

"day vs miles"

random data & miles
list(1::2)


"""
RUNNER_FILE = "runner_data_v1.txt"
def main():
    import matplotlib.pyplot as plt
   
    with open(RUNNER_FILE, "r") as infile:
        month = infile.readline()
        runner = infile.readline()
        # data type for month & runner is sting
        
    # computation
    

    
    # "split" turn from string into list; nothing in para shows split in white 
    # space
    # list of strings for each variables
    # bracket shows that they are list
    month = month.split()
    runner = runner.split()
    
    # slice; separate list of just running data
    runner_data = runner[2:]
    days = month[1:]
    
    # just the mileage from runner data
    mileage = []
    for i in range(1, len(runner_data), 2):
        mileage.append(runner_data[i])
    for i in range(1, data[i]):
         data.append(range)   
    
    # list of string to list of float
    mileage = [float(num) for num in mileage]
    
    plt.show()
        
    
    print(month)
    print(mileage)
    print(runner_data)
  
        
    plt.scatter(month, mileage)
    plt.xticks[1:31]
    plt.plot(mileage, "-o", "laney's mileage")
    plt.scatter()
    plt.scatter(x_value, )
        
  
        
    
    
main()
    