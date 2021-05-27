#!/usr/bin/env python
# -*- coding: utf-8 -*-

from views.menu import MenuView

from controllers.base import Controller

from models.joueur import JoueursModel
from models.tournois import TournoisModel


def main():
    view = MenuView()
    controller = Controller(view)
    
    controller.run()

if __name__ == '__main__':
    main()
