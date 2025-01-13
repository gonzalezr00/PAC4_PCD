#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
This module provides functionality to process a DataFrame of cyclists' data.
1. Rounds the times to the nearest multiple of 20 minutes.
2. Creates an interactive histogram of the rounded times.
3. Saves the interactive histogram as an HTML file and opens it in the default web browser.
4. Saves a static image of the histogram as a PNG file.
5. Returns the modified DataFrame with the rounded times.
'''

import os
import webbrowser
import pandas as pd
import plotly.express as px


def ex3(orbea_df: pd.DataFrame) -> pd.DataFrame:
    '''
    Rounds the times to 20-minute intervals and creates an interactive histogram.
    Parameters:
        orbea_df (pandas.DataFrame): Input DataFrame containing cyclists' data.
    '''
    def minutes_002040(x: str) -> str:
        """
        Rounds the given time to the nearest multiple of 20 minutes.
        Parameters:
            x (str): A string representing the time in the format 'HH:MM'.
        Returns:
            str: A string representing the rounded time in the format 'HH:MM'.
        """
        time = x.split(':')
        minutes = int(time[1]) // 20 * 20
        return f'{time[0]}:{minutes:02d}'

    # Aplicar la funció per arrodonir el temps
    orbea_df['time_groupped'] = orbea_df['time'].apply(minutes_002040)

    print('\nEls 15 primers valors del dataframe:')
    print(orbea_df.head(15), end='\n\n')

    # Fem un histograma dels intervals de temps
    groupped_orbea = orbea_df.groupby('time_groupped').size()

    # Es utilitza Plotly Express per crear un gràfic interactiu en format HTML
    fig = px.bar(groupped_orbea, x=groupped_orbea.index, y=groupped_orbea.values)
    fig.update_layout(title='Nombre de ciclistes per interval de temps')

    img_path = "./img/rides_histogram.html"

    # Imatge interactiv
    fig.write_html(img_path)

    # Imatge estàtica
    fig.write_image("./img/rides_histogram.png")

    # Obrir el gràfic interactiu en el navegador
    full_path = os.path.abspath(img_path)
    webbrowser.open(f'file://{full_path}', new=0)

    print(f'Gràfic interactiu guardat com {img_path} i obert automàticament al teu navegador.')
    print("Sempre pots trobar la seva versió plana a la carpeta 'img' com a png.", end='\n\n')

    return orbea_df
