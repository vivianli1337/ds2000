#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 22:26:03 2022

@author: vivian

card driver to create card objects
"""

# from [module] import [class]
from deck import Deck
from card import Card

def main():
    # Make a deck object
    deck = Deck()

    # Play WAR!!!!
    laney = 0
    john = 0
    print("Let's play WAR!!!!!")
    for i in range(0, len(deck.cards), 2):
        # Draw a card for each player
        laney_card = deck.draw()
        john_card = deck.draw()
        print("Laney got:", laney_card)
        print("John got:", john_card)
        
        # See who won the round, and if so they get a point
        if laney_card.value > john_card.value:
            laney += 1
            print("Laney wins this round!\n")
        elif john_card.value > laney_card.value:
            john += 1
            print("John cheated to win this round :(\n")
    
    # Announce the winner!
    if laney > john:
        print("Laney wins!")
    elif john > laney:
        print("John won :(")
    else:
        print("It's a tie!!!!!")

main()
    