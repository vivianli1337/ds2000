#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vivian Shu Yi Li
DS 2000
Spring 2022
Data Presentation
March 3, 2021
""" 

def main():

    import matplotlib.pyplot as plt
    import numpy as np
    
    MCDONALDS_DATA = "mcdonalds.csv"
    #initialize variables
    yum = 0
    no_yum = 0
    conv = 0
    no_conv = 0
    spic = 0
    no_spic = 0
    fat = 0
    no_fat = 0
    greas = 0
    no_greas = 0
    fas = 0
    no_fas = 0
    chp = 0
    no_chp = 0
    taste = 0
    no_taste = 0
    expen = 0
    no_expen = 0
    health = 0
    no_health = 0
    dis = 0
    no_dis = 0
    
    # step 1: gather info
    with open(MCDONALDS_DATA, "r") as infile:
        labels = infile.readline()
        
        # use while loop to find number of responses
        while True:
           answers = infile.readline()
           if answers == "":
               break
           
           # factors that we are looking at
           answers = answers.split(",")
           yummy = answers[0]
           convenient = answers[1]
           spicy = answers[2]
           fattening = answers[3]
           greasy = answers[4]
           fast = answers[5]
           cheap = answers[6]
           tasty = answers[7]
           expensive = answers[8]
           healthy = answers[9]
           disgusting = answers[10]
           
           # number of responses per factor
           if yummy == "Yes":
               yum += 1
           elif yummy == "No":
               no_yum += 1
           
           if convenient == "Yes":
               conv += 1
           elif convenient == "No":
               no_conv += 1  
        
           if spicy == "Yes":
               spic += 1
           elif spicy == "No":
               no_spic += 1 
           
           if fattening == "Yes":
               fat += 1
           elif fattening == "No":
               no_fat += 1 
           
           if greasy == "Yes":
               greas += 1
           elif greasy == "No":
               no_greas += 1 
           
           if fast == "Yes":
               fas += 1
           elif fast == "No":
               no_fas += 1 
            
           if cheap == "Yes":
               chp += 1
           elif cheap == "No":
               no_chp += 1  
            
           if tasty == "Yes":
               taste += 1
           elif tasty == "No":
               no_taste += 1 
     
           if expensive == "Yes":
               expen += 1
           elif expensive == "No":
               no_expen += 1  
               
           if healthy == "Yes":
               health += 1
           elif healthy == "No":
               no_health += 1     
        
           if disgusting == "Yes":
               dis += 1
           elif disgusting == "No":
               no_dis += 1  
                
    # bar chart
    def addlabels(x,y):
        for i in range(len(x)):
            plt.text(i,y[i],y[i], ha = "center")
            
    labels = ["yummy", "convenient", "spicy", "fattening", "greasy", 
              "fast", "cheap", "tasty", "expensive", "healthy", "disgusting"]
    pos = [yum, conv, spic, fat, greas, fas, chp, taste, expen, health, dis]
    
    neg = [no_yum, no_conv, no_spic, no_fat, no_greas, no_fas, no_chp, 
           no_taste, no_expen, no_health, no_dis]
    
    x = np.arange(len(labels))
    width = 0.4
    
    plt.bar(x-width/2, pos, width, color = "thistle", label = "yes")
    plt.bar(x+width/2, neg, width, color = "palevioletred", label = "no")
    addlabels(labels, pos)
    addlabels(labels, neg)
    
    plt.title("Thoughts about McDonalds' Food")
    plt.ylim(0,1500)
    plt.ylabel("Number of Responses")
    plt.xlabel("Factors")

    plt.xticks(x, labels)
    plt.xticks(rotation = "vertical")
        
    plt.legend(loc = "upper right")
    

    
    
    plt.show()
       
main()

