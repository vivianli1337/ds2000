#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Vivian Shu Yi Li
    DS 2000
    Spring 2022
    HW3 
    February 11, 2021
    jeopardy.py
    
test case: average amount per game
total amount / # games
1384800/41
average = 33775.61

test case: percentage of final questions correct
yes = 28 games
28/41 = 0.6829 = 68.29%
"""
def main():
    
    # step 1 gather info
    amounts = []
    results = []
    total_correct = 0
    c_amount = 0
    i_amount = 0
    
    # read files from schneider
    import matplotlib.pyplot as plt 
    with open("schneider.txt", "r") as infile:
        while True: 
            amount = infile.readline()
            result = infile.readline().strip()
                
            if amount == "" or result == "":
                break
            
            # make a 'amounts' list
            amount = float(amount)
            amounts.append(amount)
            
            # find final-jeopardy questions & amounts
            # that are correct/incorrect
            if result == "Yes":
                total_correct += 1
                c_amount += amount
            elif result == "No":
                i_amount += amount
           
            # make a 'results' list
            results.append(result)
        
    # step 2 computation
    avg = sum(amounts) / len(amounts)      
    correct = total_correct / len(results)
    p_correct = correct * 100

    # step 3 communication
    print("The average amount she won per game is $", round(avg,2))
    print("The percentage of final questions she gotten correct is", 
          round(p_correct, 2), "%.")
    
    # make a bar chart
    plt.bar(0, i_amount, color = "skyblue", label = "incorrect")
    plt.bar(1, c_amount, color = "lightpink", label = "correct")
    
    # legend & other aspects
    plt.legend()
    plt.title("Schneider Jeopardy Results")
    plt.ylabel("Total Amount in Millions")
    plt.xlabel("Results of Final Questions")
    plt.xticks([0, 1], ["Incorrect", "Correct"])
    plt.ylim(0, 1500000)
    
main()