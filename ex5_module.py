#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
This module provides functionality to process a DataFrame of cyclists' data.
1. Cleans the 'club' column in the given DataFrame.
2. Converts all club names to uppercase.
3. Removes specific substrings from the beginning and end of the club names.
4. Removes specific substrings from anywhere within the club names.
5. Strips leading and trailing whitespace from the club names.
'''

import pandas as pd

def ex5(orbea_df: pd.DataFrame) -> pd.DataFrame:
    '''
    Shows the cyclists of the UCSC (Unió Ciclista Sant Cugat) club, 
    the best cyclist of the club, and its position and percentage over the total.
    Parameters:
    orbea_df (pandas.DataFrame): DataFrame with the 'club' column to clean.
    '''
    # Quins són els ciclistes de la UCSC (Unió Ciclista Sant Cugat)?
    mask = (orbea_df['club'] == 'UCSC') | (orbea_df['club'] == 'UNIÓ CICLISTA SANT CUGAT')
    print('Dorsals dels ciclistes de la UCSC:')
    print(orbea_df[mask]['dorsal'].to_list(), end='\n\n')
    print('Ciclistes de la UCSC:')
    print(orbea_df[mask], end='\n\n')

    # Quin ciclista de la UCSC ha fet millor temps?
    millor_temps = orbea_df[mask].sort_values(by='time').head(1)
    print(millor_temps, end='\n\n')

    # En quina posició sobre el total ha quedat aquest ciclista?
    # quin percentatge sobre el total representa?
    posicio = orbea_df[orbea_df['time'] < millor_temps['time'].values[0]].shape[0] + 1
    total = orbea_df.shape[0]
    percentatge = posicio / total * 100
    print('El millor ciclista de la UCSC ha quedat' +
          f' en la posició {posicio} de {total} Top ({percentatge:.2f}%)', end='\n\n')

    return orbea_df
