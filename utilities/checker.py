#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""fields checker decorators"""

import functools

from views.utilities import UtilitiesView


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

def checker_digit_or_empy_default_field(default):
    def decorator(function):
        def wrapper(*args, **kwargs):
            while True:
                result = function(*args, **kwargs)
                if result == '':
                    return default
                elif result.isdigit():
                    return result
                else:
                    UtilitiesView().prompt_error_NaN()
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
                        UtilitiesView().prompt_error()
                else:
                    UtilitiesView().prompt_error_NaN()
            return result
        return wrapper
    return decorator
