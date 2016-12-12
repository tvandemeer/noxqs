#!/usr/bin/env python3

from objecttemplate import templatetext
from htmltemplate import templatetext


def objectpagina():
    titel = stuk['title']
    maker = stuk['principalMakers'][0]['name']
    collectie = stuk['objectCollection'][0]
    # datering hier
    if stuk['dating']['yearEarly'] != stuk['dating']['yearLate']:
        pass
    else:
        pass
    kleuren = stuk['colors']      # list object, mogelijk leeg
    omschrijving = stuk['description']
