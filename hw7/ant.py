#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 Vivian Shu Yi Li
 DS 2000
 Spring 2022
 HW7
 April 7, 2022
 ant.py
"""

import matplotlib.pyplot as plt

class Ant:
    def __init__(self, name, x = 0, y = 0, color = "magenta"):
        """ create a Card object with name(string), x. & y. position (int)
        color (string) """
        self.name = name
        self.x = x
        self.y = y
        self.color = color
        
    def draw(self):
        """ plot the ants at its x, y positions (int) with color (string)
        and the shape of your choice """
        plt.plot(self.x, self.y, "o", color = self.color, label = self.name)
        plt.legend(loc = "upper left", bbox_to_anchor = (1.05, 1.0)) 
        
    def move(self, fwd, width):
        """ return: move ants to the right by "-" steps (int) but not
        further than width - indicate the right edge (int) """
        if self.x + fwd < width:
            self.x = self.x + fwd
        else:
            self.x = width
            
    def at_edge(self, width):
        """ return boolean that says ants reached the right-edge of the board
        """
        if self.x >= width:
            return True
        else:
            return False
        
    def __str__ (self):
        """ return string used to call print() on Ant object;
        name, position, color """
        return "The winner of the race is " + str(self.name) 