#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 22:16:32 2022

@author: vivian
driver for card game

in a driver, we have out main() function, and we have a lot of object
instantiation
"""

# from [module name] import [class name]
from card import Card

def main():
    # make a card object with suit = hearts, value = 9
    c = Card("hearts", 9)
    print(c)

main()
