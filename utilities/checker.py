#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools

from views.utilities import UtilitiesView


class Checker:
    def n_is_a_number_between_x_y(self, n, x, y):
        if n.isdigit():
            if n >= x and n <= y:
                return True
            else:
                False
        else:
            return None


def checker_text_field(function):
    def wrapper(*args, **kwargs):
        while True:
            result = function(*args, **kwargs)
            if result != '':
                break
            else:
                UtilitiesView().line_separator
                UtilitiesView().prompt_error_null()
        return result
    return wrapper


def checker_digit_field(function):
    def wrapper(*args, **kwargs):
        while True:
            result = function(*args, **kwargs)
            if result.isdigit():
                break
            else:
                UtilitiesView().prompt_error_NaN()
        return result
    return wrapper


def checker_menu(x, y):
    def decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            while True:
                result = function(*args, **kwargs)
                if result.isdigit():
                    result = int(result)
                    if result >= x and result <= y:
                        break
                    else:
                        UtilitiesView().prompt_error()
                else:
                    UtilitiesView().prompt_error_NaN()
            return result
        return wrapper
    return decorator
