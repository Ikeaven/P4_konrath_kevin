#!/usr/bin/env python
# -*- coding: utf-8 -*-

from views.menu import MenuView

from controllers.base import Controller

from utilities.checker import Checker

# from models.player import PlayerModel
# from models.tournament import TournamentModel


def main():
    view = MenuView()
    checker = Checker()
    # player = PlayersModel()
    # tournament = TournamentModel()

    controller = Controller(view, checker)

    controller.run()

if __name__ == '__main__':
    main()
