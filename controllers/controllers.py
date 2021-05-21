#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TODO : Module summary
"""

from views import menuviews
from models import tournoismodel


def create_tournois():
    nom_tournois = input('Nom du tournois : ')
    tournois = tournoismodel.Tournois(nom_tournois)
    
    

def main_controller():
    """
    TODO: function summary
    """
    value = True
    while value:
        menuviews.menu_view()
        menu_value = input('entrer le numéro du menu :')

        #Créer un tournois
        if menu_value == "1":
            create_tournois()
        #quitter le programme
        elif menu_value == "5":
            value = False
        
        else :
            menuviews.value_not_defined()
        

if __name__ == "__main__":
    main_controller()


