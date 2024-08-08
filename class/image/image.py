#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 13:49:16 2022

@author: vivian
"""

import csv
import matplotlib.pyplot as plt

IMG1 = "compressed.csv"
IMG2 = "compressed2.csv"

def read_csv(filename):
    """ function: read csv
    paramter: filenmae, a strong
    returns: 2d list of string
    
    """
    data = []
    with open(filename, "r") as infile:
        csvfile = csv.reader(infile, delimiter = ",")
        for row in csvfile:
            data.append(row)
    return data

    
def decompress_img(lst):
    """ function decompress_img
        parameter: 2d list of strings, a compressed_img
        return: 2d list of strings, a uncompressed_img
    """
    
    decompressed = []
    for row in lst:
        uncompressed_row = []
        for i in range(0, len(row), 2):
            num = int(row[i])
            color = row[i + 1]
            for j in range(num):
                uncompressed_row.append(color)
            decompressed.append(uncompressed_row)
    return decompressed

def plot_img(lst):
    """ function plot_img
        parameter: 2d list of strings, an uncompressed image
        return: nothing, just plot
    """
    y= 0
    for row in lst:
        x = 0
        for color in row:
            plt.plot(x, y, "o", color = color)
            x += 1
        y -= 10


def main():
    img = input("Which file to draw? Enter 1 or 2.\n")
    if img == "1":
        imgfile = IMG1
    else:
        imgfile = IMG2
        
    compressed = read_csv(imgfile)
    decompressed = decompress_img(compressed)
    print(decompressed)
    
    plot_img(decompressed)
    
main()
         
         
         