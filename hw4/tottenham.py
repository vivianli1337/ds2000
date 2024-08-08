#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Vivian Shu Yi Li
    DS 2000
    Spring 2022
    HW4 
    February 25, 2021
    tottenham.py
"""
def main():
    FOOTBALL_FILE = "hotspur.txt"
    
    # initalize variables for fewest win and max goals:
    few_win = 40
    win_season = ""
    max_goals = 0
    max_season = ""

    # step 1: gather info from file   
    with open(FOOTBALL_FILE, "r") as infile:
        
        # use a while loop to calculate information for each year
        while True:
            year = infile.readline()
            result = infile.readline()
            if year == "" or result == "":
                break
            
            # reorganize the required data using slicing
            year = year.split()
            result = result.split()
            season = year[0]
            goals = year[1:]
            m_result = result[1:]
            
            # step 2: computation
            # convert strings into integers so we can compute
            goals = [int(x) for x in goals]
            total_matches = len(goals)
            
            first_ten = sum(goals[:10])
            last_score = sum(goals[-10:])
            
            # find wins, loses, draws using conditional statement
            # setting all variable = 0 to reset after each season
            w_matches = 0
            l_matches = 0
            d_matches = 0
            winnings = 0
            
            for i in range(0, len(m_result)):
                if m_result[i] == "W":
                    w_matches += 1
                    if goals[i] == 1:
                        winnings += 1
                elif m_result[i] == "L":
                    l_matches += 1
                elif m_result[i] == "D":
                    d_matches += 1
            
            # step 3 communicate: answering the questions
            print("How many total matches did Tottenham play in", season + "?")
            print("Tottenham played", total_matches, "matches.\n")
            
            print("How many matches did Tottenham win, lose, and draw in" + 
                  " this season?")
            print("Won:", w_matches, "matches\nLost:", l_matches, 
                  "matches\nDrawn:", d_matches, "matches.\n")
            
            print("How many matches did we win despite scoring only one goal?")
            print("Tottenham won", winnings, "matches with only one goal.\n")       
            
            print("How many total goals did we score in the first 10 games" +
                  " v.s the last 10 games of the season?")
            print("First 10 games:", first_ten, "goals.")
            print("Last 10 games:", last_score, "goals.\n")
            
            # return to step 2: compute fewest win & max goal using 
            # conditional statements
            if w_matches < few_win:
                 few_win = w_matches 
                 win_season = season
            
            sum_goals = sum(goals)
            if sum_goals > max_goals:
                max_goals = sum_goals 
                max_season = season
       
        # step 3: communicate; outside of the loop
        print("Fewest wins:", win_season)
        print("Most goals:", max_season)
            
            
            
main()