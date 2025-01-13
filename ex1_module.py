#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Module: ex1_module
    This module contains a function to read a dataset, display the first few records, 
    list the columns of the dataframe, and count the unique bikers in the dataset.
'''

import pandas as pd


def ex1():
    '''
    This function performs the following steps:
    1. Reads the dataset from a CSV file located at './data/dataset.csv'.
    2. Displays the first few records of the dataframe.
    3. Lists the columns of the dataframe.
    4. Counts and displays the number of unique bikers in the dataset.

    Returns:
        pandas.DataFrame: The dataframe containing the dataset.
    '''
    # Llegir el dataset
    path_df = './data/dataset.csv'
    orbea_df = pd.read_csv(path_df, sep=';')

    # Mostrar els primers registres i les columnes del dataframe
    print('\nDades originals:')
    print(orbea_df.head(), end='\n\n')
    print(f'Quines columnes té el dataframe?: {orbea_df.columns.to_list()}', end='\n\n')

    # Es possible que hi hagi ciclistes duplicats, per tant utilitzarem metod .unique()
    unique_bikers = orbea_df["biker"].unique()
    print(f'Quants ciclistes van participar a la prova (inicialment)?: {len(unique_bikers)}'
          , end='\n\n')

    return orbea_df  # Retornem orbea_df per utilitzar-lo a ex2
