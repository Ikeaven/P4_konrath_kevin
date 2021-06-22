#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Entry point to chess app."""

from views.menu import MenuView

from controllers.base import Controller
from controllers.routing import Router


def main():
    """Run the chess application, loop entry point."""
    menu_view = MenuView()
    router = Router()

    controller = Controller(router, menu_view)
    controller.run()


if __name__ == '__main__':
    main()
