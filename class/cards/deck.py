#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 14:07:12 2022

@author: vivian

deck class to play a game of cards
"""
import random
from card import Card

DEF_VALUES = [i for i in range(2,15)]
DEF_SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

class Deck:
    def ___init__(self, values = DEF_VALUES, suits = DEF_SUITS):
        """ make a deck object with the given values and suits """
        # cards - object; 
        self.cards = []
        for value in values:
            for suit in suits:
                c = Card(value, suit)
                self.card.append(c)
        self.shuffle()
                
    def shuffle(self):
        """ shuffle the deck of cards """
        for i in range(len(self.cards)):
            r = random.randint(0, len(self.cards) - 1)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
    
    def draw(self):
        # pop remove things from list
        """ return card at the end of the deck and remove it """
        return self.cards.pop()
        
            
            
            