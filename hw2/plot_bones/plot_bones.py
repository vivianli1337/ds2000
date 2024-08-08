#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Vivian Shu Yi Li
    DS 2000
    Spring 2022
    HW2 
    February 3, 2021
    plot_bones.py
"""
import matplotlib.pyplot as plt

def main():
    # step one: gather info from the file
    # make the file name & the markersize a constant
    FILE_ONE = "november_bones copy.txt"
    FILE_TWO = "november_nobones.txt"
    SIZE = 10
   
    print("Your file:", FILE_ONE)
    print("Your file:", FILE_TWO)
    
    # begin reading each line in first file and plot the all the days
    # give the plots in this file a specific color and marker shape 
    with open (FILE_ONE, "r") as bones:
        date = bones.readline().strip()
        number_of_days = int(bones.readline())
        x_pos = 1
        plt.plot(x_pos, number_of_days, "*", color = "deepskyblue", 
                 markersize = SIZE, label = "bones")
       
        date = bones.readline().strip()
        number_of_days = int(bones.readline())
        x_pos += 1
        plt.plot(x_pos, number_of_days,"*", color = "deepskyblue", 
                 markersize = SIZE)
    
        date = bones.readline().strip()
        number_of_days = int(bones.readline())
        x_pos += 1
        plt.plot(x_pos, number_of_days,"*", color = "deepskyblue", 
                 markersize = SIZE)
    
        date = bones.readline().strip()
        number_of_days = int(bones.readline())
        x_pos += 1
        plt.plot(x_pos, number_of_days,"*", color = "deepskyblue", 
                 markersize = SIZE)
    
    # begin reading each line in second file and plot the all the days
    # give the plots in this file a different specific color and marker shape
    with open (FILE_TWO, "r") as no_bones:
        date = no_bones.readline().strip()
        number_of_days = int(no_bones.readline())
        x_pos = 1
        plt.plot(x_pos, number_of_days, "x", color = "black", 
                 markersize = SIZE, label = "no bones")
          
        date = no_bones.readline().strip()
        number_of_days = int(no_bones.readline())
        x_pos += 1
        plt.plot(x_pos, number_of_days,"x", color = "black", 
                 markersize = SIZE)
       
        date = no_bones.readline().strip()
        number_of_days = int(no_bones.readline())
        x_pos += 1
        plt.plot(x_pos, number_of_days,"x", color = "black", 
                 markersize = SIZE)
       
        date = no_bones.readline().strip()
        number_of_days = int(no_bones.readline())
        x_pos += 1
        plt.plot(x_pos, number_of_days,"x", color = "black", 
                 markersize = SIZE)
        
    # label the axes
    plt.xlabel("November")
    plt.ylabel("Number of Days")
    # give the graph a title
    plt.title("Number of Bones or No Bones Days per week")
    
    # Change the range of the axis
    plt.ylim(0,7)
    plt.xlim(0,5)
    # make a legend 
    plt.legend(loc = "lower right")

main()



