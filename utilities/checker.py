#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Checker:
    def string_is_a_number(self, var_to_check): 
        if var_to_check.isdigit():
            return True
        else:
            return False