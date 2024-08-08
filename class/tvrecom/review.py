#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 13:21:42 2022

@author: vivian
    Review class --- to rep a person's review of a show
"""
class Review:
    def __init__(self, name, title, rating, platform = "Netflix",
                 times_watched = 1):
        ''' Create a Review object with the given attributes '''
        self.name = name
        self.title = title
        self.platform = platform
        self.rating = rating
        self.times_watched = times_watched

    def __str__(self):
        ''' return a pretty string of the review'''
        return self.title + "--" + str(self.rating)
    
    def __eq__(self, other):
        if self.title == other.title:
            return True
        return False