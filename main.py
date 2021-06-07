#!/usr/bin/env python
# -*- coding: utf-8 -*-

from views.menu import MenuView
from views.player import PlayerView
from views.tournament import TournamentView

from controllers.base import Controller


def main():
    menu_view = MenuView()
    player_view = PlayerView()
    tournament_view= TournamentView()

    controller = Controller(menu_view, player_view, tournament_view)
    controller.run()


if __name__ == '__main__':
    main()
