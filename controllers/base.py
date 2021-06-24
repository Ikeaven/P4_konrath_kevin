#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Base Controller."""


class Controller:
    """Main Controller, it start the main loop app !
    """

    # init
    def __init__(self, router, menu_view):
        """Init Controller.

        Args:
            router,
            menu_view
        """
        # Routes
        self.router = router

        # views
        self.menu_view = menu_view

    def run(self):
        """App loop."""
        while True:
            selected_menu = self.menu_view.display_menu()
            main_menu_return = self.router.main_menu(selected_menu)
            if main_menu_return is False:
                break
