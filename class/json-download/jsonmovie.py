#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 13:25:24 2022

@author: vivian

creating movies from a JSON file

"""
import json
from movie import Movie
import matplotlib.pyplot as plt

MOVIE = "movie.json"

def read_json(filename):
    """ function read_json
    parameter: filename, a strong
    return: list of dictionaries, one per movie
    """
    with open(filename, "r") as infile:
        data = json.load(infile)
    
    # figure out the structure of the filie
    print("Data is type...", type(data))
    for key, value in data.items():
        print(key)
    
    # what's in the value for key results?
    results = data("results")
    print(type(results))
    
    # what is in the result list?
    print("Result is a list of...", type(results[0]))
    
    # take a look at results
    print("The keys in results are ....")
    for d in results:
        for key, value in d.items():
            print(key, "----", value)
        print()

def make_movie_objs(list_of_dicts):
    """
    """
    movies = []
    for d in list_of_dicts:
        title = d["title"]
        vote = d["vote average"]
        date = d["release_date"]
        m = Movie(title, vote, date)
        movies.append(m)
    return movies


    
def main():
    # step 1: gather data fron the JSON file
    data = read_json(MOVIE)
    print(data)
    
    # step 2: computation (make movie objects)
    movie = make_movie_objs(data)
    for movie in Movie:
        print(movie)
    
    # step 3: plot year vs vote
    year = [m.year for m in movies]
    votes = [m/vote for m in movies]
    plt.scatter(year, votes, "o", color = "magenta")
    
main()