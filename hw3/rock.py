#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Vivian Shu Yi Li
    DS 2000
    Spring 2022
    HW3 
    February 11, 2021
    rock.py
"""
def main():
    
    import matplotlib.pyplot as plt
    import random
    
    # step 1: gather info
    rachlin_result = 0
    strange_result = 0
    tie = 0
    rachlin_throw = ""
    strange_throw = "rock"
    s_previous = ""
    
    # create a loop for the game
    while True:
    
        # first game, we assume that if strange throw a rock (default)
        # then, rachlin would throw a paper
    
        s_previous = strange_throw
          
        if s_previous == "rock":
            rachlin_throw = "paper"
        elif s_previous == "paper":
            rachlin_throw = "scissors"
        else:
            rachlin_throw = "rock"
        
        # after first game, the code "s_previous = strange_throw" would
        # take the strange's throw from the random as s_previous -> loop
        random_throw = random.randint(1,10)
        
        if random_throw == 1:
            strange_throw = "scissors"
        elif random_throw == 2 or random == 3:
            strange_throw = "paper"
        else:
            strange_throw = "rock"   
        
        # winning results based on strange's & rachlin's moves
        if rachlin_throw == "scissors" and strange_throw == "rock":
            strange_result += 1
        elif rachlin_throw == "paper" and strange_throw == "scissors":
            strange_result += 1
        elif rachlin_throw == "rock" and strange_throw == "paper":
            strange_result += 1
        elif strange_throw == rachlin_throw:
            tie += 1
        else:
             rachlin_result += 1    
        
        # to stop the game at 10000
        if strange_result == 10000 or rachlin_result == 10000:
            break
        
    # winner wins the prize aka coffee
    if strange_result > rachlin_result:
        print("Strange wins the coffee prize!")
    elif rachlin_result > strange_result:
        print("Rachlin wins the coffee prize!")
    
    # communication
    print("Strange won", strange_result, "games.\n")
    print("Rachlin won", rachlin_result, "games.\n")
    print("They were tied for", tie, "games.")
        
    # make a bar graph
    plt.bar(0, rachlin_result, color = "skyblue", label = "Rachlin wins")
    plt.bar(1, strange_result, color = "lightgreen", label = "Strange wins")
    plt.bar(2, tie, color = "lightpink", label = "tie")
    
    # legend & other aspects
    plt.legend()
    plt.title("Rock, Paper, Scissor Results")
    plt.ylabel("Number of Games")
    plt.xlabel("Results")
    plt.xticks([0, 1, 2], ["Rachlin wins", "Strange wins", "Tie"])
    plt.ylim(0, 11000) 
    
main()
