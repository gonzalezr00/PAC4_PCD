#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
This module provides the main funtionality for the project.
Each exercise is executed in a separate module.
In order to obtain the final DataFrame, the main function calls each module.
It will only be executed if this file is the main file.
'''

from ex1_module import ex1
from ex2_module import ex2
from ex3_module import ex3
from ex4_module import ex4
from ex5_module import ex5


def main():
    '''
    Main function to execute the exercises
    '''
    # Executar cada exercici per a actualitzar el dataframe
    orbea_df = ex1()
    orbea_df = ex2(orbea_df)
    orbea_df = ex3(orbea_df)
    orbea_df = ex4(orbea_df)
    orbea_df = ex5(orbea_df)

# Executar el programa principal sols si aquest fitxer és l'arxiu principal
if __name__ == "__main__":
    main()
