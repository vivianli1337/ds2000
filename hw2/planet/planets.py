o#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 Vivian Shu Yi Li
 DS 2000
 Spring 2022
 HW2 
 February 3, 2021
 planet.py
"""
"""
test case 1: mercury and venus
Mercury to Sun = 113.111 units
Venus to Sun = 231.138 units
Average = 172.125 units

test case 2: earth and pluto
Pluto to Sun = 972.594 units
Earth to Sun = 493.138 units
Average = 732.866 units
    
"""
import matplotlib.pyplot as plt

def main():
    # step one: gather the month from the user and read from the file
    
    # define the constant variables
    SX_POS = 100
    SY_POS = -100
    S_MARKERSIZE = 20
    S_COLOR = "yellow"
    plt.plot(SX_POS, SY_POS, marker = "o", color = S_COLOR, 
             markersize = S_MARKERSIZE, label = "sun")
    
    # ask user for planets & gather info from respective file
    planet_one = input("Enter the name of the planet.\n")
    planet_two = input("Enter the name of the other planet.\n")
    file_one = planet_one + ".txt"
    file_two = planet_two + ".txt"
   
    print("Your file:", file_one)
    print("Your file:", file_two)
    
    # begin reading each file
    with open (file_one, "r") as planets:
        # read the coordinates in the file 
        x_axis_i = int(planets.readline().strip())
        y_axis_i = int(planets.readline().strip())
        
        # conditional statetement: color, size of planet that the user input
        if planet_one == "venus":
            markersize = 5
            color = "orange"
        elif planet_one == "mercury":
            markersize = 3
            color = "red"
        elif planet_one == "earth":
            markersize = 12 
            color = "blue"
        else:
            markersize = 8 
            color = "purple"
        
        # plotting the planet
        plt.plot(x_axis_i, y_axis_i, marker = "o", color = color, 
                 markersize = markersize, label = planet_one)
    
    with open (file_two, "r") as planets:  
        # read the coordinates in the file and plot them
        x_axis_ii = int(planets.readline().strip())
        y_axis_ii = int(planets.readline().strip())
        
        # conditional statetement: color, size of planet that the user input
        if planet_two == "venus":
            markersize = 5 
            color = "orange"
        elif planet_two == "mercury":
            markersize = 3 
            color = "red"
        elif planet_two == "earth":
            markersize = 12 
            color = "blue"
        else:
            markersize = 8 
            color = "purple"
        
        # plotting the planet    
        plt.plot(x_axis_ii, y_axis_ii, marker = "o", color = color, 
                 markersize = markersize, label = planet_two)
    
    # label the axes
    plt.xlabel("x-coordinate of the planet")
    plt.ylabel("y-coordinate of the planet")
    plt.xlim(-250, 300)
    plt.ylim(-200, 900)
    # give the graph a title
    plt.title("The Distance Between the Sun and the Planets")
    
    
    # legends
    plt.legend(loc = "upper right")
    
    # step 2: calculating the Euclidean distance
    sun_to_one = round((((SX_POS - x_axis_i) ** 2 + 
                         (SY_POS - y_axis_i) ** 2) ** 0.5), 3)
    sun_to_two = round((((SX_POS - x_axis_ii) ** 2 + 
                         (SY_POS - y_axis_ii) ** 2) ** 0.5), 3)
    avg_dis = round(((sun_to_one + sun_to_two) / 2), 3)
     
    
    # step 3: communicate
    print("The euclidean distance between", planet_one, "and the Sun is", 
          sun_to_one, "units.")
    print("The euclidean distance between", planet_two, "and the Sun is", 
          sun_to_two, "units.") 
    print("The average distance is", avg_dis, "units.")
    
main()



    