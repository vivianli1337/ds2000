#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Vivian Shu Yi Li
    DS 2000
    Spring 2022
    HW7
    April 7, 2022
    racetime.py
"""
# from [module] import [class]
from ant import Ant

import random

import matplotlib.pyplot as plt

import time

# make a list of the ants' names and colors
name = ["Artemis", "Aurora", "Diana", "Lucian", "Luna", "Naomi", 
        "Solana", "Selene", "Stella"]

color = ["silver", "aquamarine", "orange", "powderblue", "mediumpurple",
         "indigo", "violet", "pink", "paleturquoise"]

width = 150

p_winner = []

def ant_obj(name, color):
    """ function ant_object
        parameter: name (list of string), color (list of string)
        return: a list of 9 ant objects w/ name, position < 100, color
    """
    ants = []
    
    for i in range(len(name)):
        ants_obj = Ant(name[i], 0, random.randint(0,150), color[i])
        ants.append(ants_obj)
        
    return ants
        
def steps(ants):
    """ function steps
        parameter: list of ant names and auto choose random number of steps
        for each ants
        return: # of steps (int) that the ants moved toward the right
    """
    for ant in ants:
        ant.move(random.randint(0,10), width)

def show(ants):
    """ function show
        paramter: list of ant names
        return: show ants on the screen
    """
    for ant in ants:
        ant.draw()

def pro_winner(ants):
    """ function winner
        parameter: a list of ants
        return: the potential winner of the name
    """
    for ant in ants:
        if ant.at_edge(width) == True:
            p_winner.append(ant)
            break
    return p_winner 

def winner():
    """ function winner
        parameter: blank --- find the final winner
        return: the name of the final winner (string)
    """
    final_winner = p_winner[0]
    for winner in p_winner:
        if winner.x > final_winner.x:
            winner = final_winner 
    
    print(final_winner)
            
def plot_ants():
    """ function plot_ants
        parameter: blank ----
        return: nothing, just organizing plots
    """

    plt.xlabel("Distance")
    plt.xlim(0, width + 1)
    plt.ylim(0, width)
    plt.title("Let the Ant Race Begin!")
    plt.show()
    
def main():
    # step 1: save the racer info
    racers = ant_obj(name, color)

    # step 2: computation
    # use the call functions to show each ant's movement
    while len(p_winner) == 0:
        plot_ants()
        steps(racers)
        show(racers)
        time.sleep(0.5)
        pro_winner(racers)
        
    # step 3: communication
    winner()    
       
main()
