#!/usr/bin/env python
# -*- coding: utf-8 -*-

from views.menu import MenuView

from controllers.base import Controller

from utilities.checker import Checker


def main():
    view = MenuView()
    checker = Checker()
    controller = Controller(view, checker)

    controller.run()

if __name__ == '__main__':
    main()
