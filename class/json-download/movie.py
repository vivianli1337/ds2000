#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 14:09:47 2022

@author: vivian
"""

class Movie:
    def ___init__(self, title, vote, date, year):
        """ make a movie object"""
        self.title = title
        self.vote = vote
        self.date = date
        self.year = year
    
    def __str__(self):
        """ return a pretty string of the object"""
        return self.title + "--" + self.date
    
    def get_year(self):
        """ return the uear as an int"""
        lst = self.date.split("-")
        return int(lst[0])
    