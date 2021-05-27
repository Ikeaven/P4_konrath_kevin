#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Tournament:

    LISTE_TOURNOIS = []

    def __init__(self, tournois_infos):
        for attr_name, attr_value in tournois_infos.items():
            setattr(self, attr_name, attr_value)

