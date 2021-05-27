#!/usr/bin/env python
# -*- coding: utf-8 -*-

from views.menu import MenuView
from views.playerinfo import GetPlayerInfoView
from views.tournamentinfo import GetTournamentInfoView

from controllers.base import Controller


def main():
    menu_view = MenuView()
    get_player_info_view = GetPlayerInfoView()
    get_tournament_info_view = GetTournamentInfoView()

    controller = Controller(menu_view, get_player_info_view, get_tournament_info_view)
    controller.run()


if __name__ == '__main__':
    main()
