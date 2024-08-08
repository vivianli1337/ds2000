#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 14:10:34 2022

@author: vivian


data from amy's winning streak on jeopardy
task #1 - how much did she win?
test case: in real life it was ~1.38 mill'
"""

FILENAME = "schneider.txt"
import matplotlib.pyplot as plt 

def main():
    amounts = []
    
    # step one: gather data fron the file
    # asusume amount, yes/bno, amount, yes/no
    with open(FILENAME, "r") as infile:
        while True: #special python variable
            amount = infile.readline()
            final = infile.readline()
            
            # IF AMOUNT OR FINAL IS EMPTY,
            #it must the the end of the file
            # so stop the oop
            if amount == "" or final == "":
                break
            
            # if i gt this far, then amount 
            # and final must have valid data
            # step 2 computation
            amount = float(amount)
            # final = final.strip() #get rid of line break
            amounts.append(amount)
   
    # step 2: computations
    # compare first 3 games to last 3 games
    # there are 41 games in total
    first_three = amounts[0] + amounts[1] + amounts[2]
    last_three = amounts[38] + amounts[39] + amounts[40]
    
    # get the min and max of the amounts won
    max_won = max(amounts)
    min_won = min(amounts)
    
    low = 25000
    medium = 45000
    low_count = 0
    medium_count = 0
    high_count = 0
    for amount in amounts:
        if amount <= low:
            low_count += 1
        elif amount <= medium:
            medium_count += 1
        else:
            high_count += 1
    
    game_cats = [low_count, medium_count, high_count]
    
    # step 3: communicate
    # sanity-check by printing out list
    print(amounts)
    print("Amount won in first three games:", round(first_three))
    print("Amount won in last three games:", round(last_three))
    print("The max is", max_won, "and the low is", min_won)
    print("Low game:", low_count, "\n Medium games:", medium_count,
          "\n High games:", high_count)
    
    # create a plot for the categories of games (high/low/med)
    
    plt.bar([0, 1, 2], game_cats, color = ["aqua", "limegreen", "fuchsia"])
    
    plt.legend()
    plt.title("Schneider Jeopardy Results!")
    plt.ylabel("Number of games")
    plt.xticks([0, 1, 2], ["Low-scoring", "Med-scoring", "High-Scoring"])
    
    # sep = separater; no space
                
main()

