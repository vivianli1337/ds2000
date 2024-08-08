# -*- coding: utf-8 -*-
"""
  Vivian Shu Yi Li
  DS 2000
  Spring 2022
  HW5
  March 11, 2022
  qr.py
"""
import csv
import matplotlib.pyplot as plt

CODE = "positions.csv"

def read_csv(filename):
    """ function: read csv
    paramter: filename, a string
    returns: 2d list of data in string
    
    """
    # open file & gather info into a list - full of given numbers
    data = []
    with open(filename, "r") as infile:
        csvfile = csv.reader(infile, delimiter = ",")
        for row in csvfile:
            data.append(row)
    return data

def qr_code(lst):
    """ function qr_code
        parameter: 2d list of strings of numbers
        return: 2d list of integers
    """
    # create a list for the entire data and a sublist for each row
    qr_int = []
    for row in lst:
        s_num = []
        
        # convert strings into integers and add them to sublist
        for i in range(0, len(row)):
            num = int(row[i])
            s_num.append(num)
        
        # add all sublist into the list for entire data
        qr_int.append(s_num)
    return qr_int

def plot_img(lst):
    """ function plot_img
        parameter: 2d list of integers for the qr code
        return: nothing, just plot
    """
    # starting at y = 0, plot each row and color them accordingly 
    y = 0
    
    # create a list of int to be magenta color
    for row in lst:
        magenta_int = row
        magenta_list = []
        
        # add the magenta number to the list & plot them
        for x in magenta_int:
            magenta_list.append(x)
            plt.plot(x, y, "s", color = "black", markersize = 10)
        
        # use the 'not in' operator to plot the other numbers in another color
        for num in range(0,37):
            if num not in magenta_list:
                plt.plot(num, y, "s", color = "white", markersize = 10)
        
        # change the y-coord for the next row
        y -= 1


def main():
    # call functions & create variables to remember them    
    info = read_csv(CODE)
    qr_num = qr_code(info)
    plot_img(qr_num)
    
    
main()
    