#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 21:23:32 2022

@author: vivian

card class -- needs suit, value attributes
"""

class Card:
    def __init__(self, suit, value):
        # suit, value are parameters
        # self.suit, self.val area attributes
        """ create a Card object with read suit (string and value (int)) """
        # create carrd object w/ req'd value (int) and suit (string)
        self.value = value
        self.suit = suit
        
    def __str__(self):
        """ rerturn a pretty string version of the object repping the card """
        return str(self.value) + " of " + self.suit
    