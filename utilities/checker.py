#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""fields checker decorators"""

import functools
import datetime

# TODO ajouter les checkers a filds directement... 

from views.utilities import UtilitiesView


def checker_text_field(function):
    def wrapper(*args, **kwargs):
        while True:
            result = function(*args, **kwargs)
            if result != '':
                break
            else:
                UtilitiesView().line_separator
                UtilitiesView().display_error_null()
        return result
    return wrapper


def checker_digit_field(function):
    def wrapper(*args, **kwargs):
        while True:
            result = function(*args, **kwargs)
            if result.isdigit():
                break
            else:
                UtilitiesView().display_error_NaN()
        return result
    return wrapper


def checker_digit_or_empy_default_field(default):
    def decorator(function):
        def wrapper(*args, **kwargs):
            while True:
                result = function(*args, **kwargs)
                if result == '':
                    print(f'Valeur mise à {default}')
                    return default
                elif result.isdigit():
                    return result
                else:
                    UtilitiesView().display_error_NaN()
        return wrapper
    return decorator


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
                        UtilitiesView().display_error()
                else:
                    UtilitiesView().display_error_NaN()
            return result
        return wrapper
    return decorator


def date_validation(function):
    def wrapper(*args, **kwargs):
        while True:
            result = function(*args, **kwargs)
            try:
                datetime.datetime.strptime(result, "%d/%m/%Y")
                break
            except ValueError:
                UtilitiesView().display_error()
        return result
    return wrapper


def sex_validation(function):
    def wrapper(*args, **kwargs):
        while True:
            result = function(*args, **kwargs)
            if result == 'M' or result == 'F':
                break
            else:
                UtilitiesView().display_error()
        return result
    return wrapper
