# File name: load_data.py
# Author: Bertram Hage, Johannes Nielsen
# Date: January 19, 2023
# Description: This script provides a function for reading a csv file to load the data.

import pandas as pd

def load_data(filename):
    #Load data into pandas with apropriate column names
    #Returns a pandas dataframe with the data
    
    grades = pd.read_csv(filename, sep=",")

    return grades

