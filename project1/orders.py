# -*- coding: utf-8 -*-
"""
Vivian Shu Yi Li
DS 2000
Spring 2022
Data Presentation
March 3, 2021
officesupplies.py

which region orders the most supplies
which region order the most units 

"""

def main():
    import matplotlib.pyplot as plt
    
    SUPPLIES_DATA = "OfficeSupplies.csv"
    east = 0
    central = 0
    west = 0
    total_loc = []
   
    with open(SUPPLIES_DATA, "r") as infile:    
        title = infile.readline()
        
        while True:
            order = infile.readline()
            if order == "":
                break
            order = order.split(",")
            location = order[1]
            
            
            if location == "East":
                east += 1
            elif location == "Central":
                central += 1
            elif location == "West":
                west += 1
      
        total_loc = [east, west, central]
        print(total_loc)
        
        plt.bar(0, east, color = "skyblue")
        plt.bar(1, west, color = "lightgreen")
        plt.bar(2, central, color = "lightpink")
        
        plt.title("Office Supplies Orders from July 2014 - July 2015")
        plt.ylabel("Number of Orders")
        plt.xlabel("Region")
        plt.xticks([0, 1, 2], ["East", "West", "Central"])
        plt.ylim(0, 30)
           
    
main()