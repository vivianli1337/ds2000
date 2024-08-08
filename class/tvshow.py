#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 13:18:15 2022

@author: vivian
"""


import matplotlib.pyplot as plt
import random
      
def main():
    count = 0
    while count < 10:
    # step one: gather data by randomly generating 
    # episode numbers and season #s
        season = random.randint(1,7)
        if season == 1:
            ep = random.randint(1,12)
        else:
            ep = random.randint(1,22)

  
        # step 2: computations
        # change default height, color, and markersize
        # depending on which episode we're looking at
        height = 5
        markersize = 10
        color = "yellow"
    
    # season finales is pretty good
        if ep == 12 and season == 1:
            height += 3
            color = "greenyellow"
            markersize += 3
        elif season != 1 and ep == 22:
            height += 4
            color = "springgreen"
            markersize += 4
        
    
    # season 4 is pretty good, with two excellent eps
        if season == 4:
            if ep ==9 or ep == 10:
                height += 5
                color = "lime"
                markersize += 5
            else:
                height += 3
                color = "greenyellow"
                markersize += 5
            
    # after season 5 it got worse except the musical
        if season > 5:
            if season == 6 and ep == 5:
                height += 7
                color = "magenta"
                markersize += 7
            else:
                height -= 4
                color = "firebrick"
                markersize -= 4
    
    # communicate 
        print("season:", season, "episode:", ep)
        plt.plot(season * 22 + ep, height, "o", color = color, markersize = markersize)
        plt.ylim(0, 12)
        plt.xlim(22, 200)
    
    #increment the count to repeat the loop
        count += 1
    
    
main()


