#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 13:36:32 2022

@author: vivian
"""
import csv
from review import Review
# review = module

REVIEWS = "reviews_sec2.csv"

def csv_to_dict(filename):
    """
    function: csv_to_dicts
    parameter: filename, a string
    returns: list of dictitoanries, which each one is a review and 
    keys = name, title, platform, etc
    and values = person's name, show's title, etc
    """
    data = []
    with open(filename, "r") as infile:
        csvfile = csv.reader(infile, delimiter = ",")
        keys = next(csvfile)
        for row in csvfile:
            d = {}
            for i in range(len(row)):
                d[keys[i]] = row[i]
            data.append(d)
    return data

def make_review_objs(list_of_dict, person):
    ''' Function: make_review_objs
        Parameter: list of dictionaries wheere one dictionary = one show
        and a person's name
        Returns: list of Review objects
    '''
    reviews = []
    for item in list_of_dict:
        name = item["Name"]
        if name == person:
            title = item["Title"]
            rating = int(item["Rating"])
            review = Review(name, title, rating)
            reviews.append(review)
    return reviews
                

def make_recommendation(laney_review, friend_reviews):
    ''' Function: make_recomkmendation
        Parameters: list of Reivew objs (Laney), list of review objs (recommender)
        Returns: list of review objs (recommended shows)
    '''
    recs = []
    for review in friend_reviews:
        if review.rating > 3 and review not in laney_review:
            recs.append(review)
    return recs
 
def shows_in_common(laney, friend):
    """ function shows_in_common
    parameter: 2 lists of review objects (laney and recommender)
    return: # of shows in common
    """
    count = 0
    for review in laney:
        if review in friend:
            count += 1
    return count

def main():
   
    reviews = csv_to_dict(REVIEWS)
    # print(reviews)

    # make a list of objects for laney's reviews    
    laney_objs = make_review_objs(reviews, "Laney")
    for review in laney_objs:
        print(review)
    
    # make a list of objects for laney's friend
    friend = input("Who is recommending to Laney?\n")
    friend_objs = make_review_objs(reviews, friend)
       
    # get numbeer of shows in common
    in_common = shows_in_common(laney_objs, friend_objs)
    if in_common == 0:
        print("You and", friend, "have nothing in common, but "
              "here some recommendations....")
    elif in_common == 1:
        print("You might want to watch...")
    
    else:
        print("You should DEFINITELY watch...")
        
    # Call the recommender function
    recs = make_recommendation(laney_objs, friend_objs)
   
    # Step three --- communicate! Print out recommendations
    print(friend, "thinks you should watch...")
    for rec in recs:
        print(rec)
   
main()