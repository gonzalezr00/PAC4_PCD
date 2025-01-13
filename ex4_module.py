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

def ex4(orbea_df: pd.DataFrame) -> pd.DataFrame:
    '''
    Cleans the 'club' column in the given DataFrame.
    
    Parameters:
    orbea_df (pandas.DataFrame): DataFrame with the 'club' column to clean.
    '''
    def cleaner_club_name(df: pd.DataFrame) -> pd.DataFrame:
        '''
        Cleans the 'club' column in the given DataFrame by performing the following operations:
        Parameters:
        df (pandas.DataFrame): The DataFrame containing the 'club' column to be cleaned.
        Returns:
        pandas.DataFrame: The DataFrame with the cleaned 'club' column.
        '''
        # Netejar el nom del club
        df['club'] = df['club'].str.upper()

        # Llistes de patrons a eliminar
        elim_list = [
            'PEÑA CICLISTA ', 'PENYA CICLISTA ', 'AGRUPACIÓN CICLISTA ', 
            'AGRUPACION CICLISTA ', 'AGRUPACIÓ CICLISTA ', 'AGRUPACIO CICLISTA ', 
            'CLUB CICLISTA ', 'CLUB '
        ]
        elim_regex_inici = [
            'C.C. ', 'C.C ', 'CC ', 'C.D. ', 'C.D ', 'CD ', 'A.C. ', 'A.C ', 
            'AC ', 'A.D. ', 'A.D ', 'AD ', 'A.E. ', 'A.E ', 'AE ', 'E.C. ', 
            'E.C ', 'EC ', 'S.C. ', 'S.C ', 'SC ', 'S.D. ', 'S.D ', 'SD '
        ]
        elim_regex_fi = [
            ' T.T.', ' T.T', ' TT', ' T.E.', ' T.E', ' TE', ' C.C.', ' C.C', 
            ' CC', ' C.D.', ' C.D', ' CD', ' A.D.', ' A.D', ' AD', ' A.C.', 
            ' A.C', ' AC'
        ]

        # Utilitzar expressions regulars per eliminar patrons de text
        pattern = "|".join(
            [f"^{elim}" for elim in elim_regex_inici] +
            elim_list +
            [f"{elim}$" for elim in elim_regex_fi]
        )
        df['club'] = df['club'].str.replace(pattern, '', regex=True)

        # Eliminar espai en blanc al principi i al final
        df['club'] = df['club'].str.strip()
        return df

    # Aplicar la funció de neteja del nom del club
    orbea_df = cleaner_club_name(orbea_df)
    print(orbea_df.head(15), end='\n\n')

    return orbea_df
