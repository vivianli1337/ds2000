#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 13:50:38 2022

@author: vivian


practicing w/ pandas with presidential election data
- import pandas as pf
- pd.read_csv
- df.head()
- df.describe()
- df = df[["col1", "col2"]]
- df = df.groupby(["col1", "col2"])
"""
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio
from plotly.offline import plot

PRES = "1976-2020-president.csv"


def main():
    # step 1 read in from the file into a dataframe
    # \t = tab
    df = pd.read_csv(PRES, sep = "\t")
    
    # dataframe
    print(df)
    
    # get a peek of what's in the file
    # method
    print(df.head(20))
    
    # what are the columns?
    # attribute
    print(df.columns)
    
    # summary of numeric data
    # method
    print(df.describe())
    
    # what are the data types?
    # attribute
    # make everything a string cuz of different data types
    # objects mean string
    # number (64 [bits]) means the amount of space the data is thinking
    print(df.dtypes)
    
    # keep only the columns we like
    df = df[["year", "state", "candidate", "candidatevotes", 
             "party_simplified"]]
    print(df.head(20))
    # see individual column
    print(df["candidate"].head(20))
    
    # use groupby: group  by year and party
    # use .sum to find the total
    # reset_index ---> show the row number
    df = df.groupby(["year", "party_simplified"]).sum().reset_index()
    print(df.head(20))
    
    # switched position; group by party first and then year
   ## df = df.groupby(["party_simplified", "year"]).sum().reset_index()
   ## print(df.head(20))
    
    # sort within each year by candidatevotes
    df = df.sort_values(by = ["year", "candidatevotes"])
    print(df.head(20))
    
    # set rid of any row where the party is not a dem or repub
    # | means or
    df = df[(df["party_simplified"] == "DEMOCRAT") | (df["party_simplified"] == "REPUBLICAN")]
    df = df.sort_values(by = ["year", "party_simplified"])
    print(df)
    
    
    # make a list of dem votes using df.loc
   ## dems = df.loc[df["party_simplified"] == "DEMOCRAT", "candidatevotes"]
   ## reps = df.loc[df["party_simplified"] == "REPUBLICAN", "candidatevotes"]
    
    # get distinct years; ignore duplicates
   ## years = df["year"].unique()
    
    # make a line chart of votes
   ## plt.plot(years, dems, "-o", color = "blue")
   ## plt.plot(years, reps, "-o", color = "red")
    
    # make an interactive chart in plotly
    # for color => how to distinguish 2 y values & ensure that color for each
    # group are the same
    pio.renderers.default = "browser"
    fig = px.line(x = df["year"], y = df["candidatevotes"], 
                  color = df["party_simplified"])
    fig.update_traces(mode = "markers+lines", hovertemplate = None)
    fig.update_layout(hovermode = "x unified")
    plot(fig)
    
    
    
    
main()
