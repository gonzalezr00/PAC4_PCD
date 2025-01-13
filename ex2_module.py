#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
This module provides functionality to process a DataFrame of cyclists' data.
The main function `ex2` performs the following tasks:
1. Removes rows where the 'time' column is equal to '00:00:00'.
2. Replaces the names in the 'biker' column with unique fake names using the Faker library.
3. Prints the number of unique participants before and after the name replacement.
4. Prints the first few rows of the modified DataFrame.
5. Prints the information of the cyclist with dorsal number 100.
'''

import pandas as pd
from faker import Faker
import numpy as np


def ex2(orbea_df: pd.DataFrame) -> pd.DataFrame:
    '''
    Processes the input DataFrame by removing specific rows and replacing names with fake names.
    Parameters:
        orbea_df (pandas.DataFrame): Input DataFrame containing the cyclists' data.
    '''
    # Eliminar 'time' igual a '00:00:00'
    elim = orbea_df['time'] == '00:00:00'
    orbea_df = orbea_df[~elim]

    # Esperem que el nombre de participants disminueixi
    print(
        "Quants ciclistes van participar a la prova (després d'eliminar '00:00:00')?: "
            + f"{len(orbea_df['biker'].unique())}", end='\n\n'
    )

    # Obtindre el nou nombre de participants únics
    num_part_ini = len(orbea_df['biker'].unique())

    # Funció per reemplaçar els noms per noms falsos
    def name_surname(df):
        """
        Replaces the 'biker' names in the given DataFrame with unique fake names.

        Args:
            df (pandas.DataFrame): Input DataFrame with participant names.

        Returns:
            pandas.DataFrame: The DataFrame with the 'biker' names replaced by unique fake names.
        """
        list_participants = df['biker'].unique()
        faker = Faker()

        # Inicialitzar un conjunt per verificar unicitat
        unique_names = set()

        # Generar noms falsos únics sense repetició
        while len(unique_names) < len(list_participants):
            unique_names.add(faker.name())

        # Convertir el conjunt de noms a un array numpy
        list_fakes = np.array(list(unique_names))

        # Reemplaçar els noms al DataFrame
        names = dict(zip(list_participants, list_fakes))
        df.loc[:, 'biker'] = df['biker'].replace(names)

        return df

    # Aplicar la funció de canvi de nom
    orbea_df = name_surname(orbea_df)

    # Verificar que el nombre de participants únics segueix sent el mateix
    num_part_fi = len(orbea_df['biker'].unique())
    print(f'Quants ciclistes tenim ara en el dataframe?: {num_part_fi} \n')

    if num_part_ini == num_part_fi:
        print("La quantitat de participants únics no ha canviat!")
    else:
        print("La quantitat de participants únics ha canviat!")

    # Informació del dataframe i del ciclista amb dorsal 100
    print()
    print(orbea_df.head())
    print(f'\nCiclista amb dorsal 100: \n{orbea_df[orbea_df["dorsal"] == 100]}')

    return orbea_df
