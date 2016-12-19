#!/usr/bin/env python3

from client import object_info
from objecttemplate import templatetext
import sys

import argparse
from urllib.parse import urlparse, parse_qs

parser = argparse.ArgumentParser()
# add arguments
args = parser.parse_args()
artobject = object_info(sys.argv[1])    # Eerste command line argument is object id

def maak_objectpage():
    afbeelding = artobject['webImage']['url']
    titel = artobject['title']
    maker = artobject['principalMakers'][0]['name']
    collectie = artobject['objectCollection'][0]
    if artobject['dating']['yearEarly'] != artobject['dating']['yearLate']:
        datering = '%s - %s' % (artobject['dating']['yearEarly'], artobject['dating']['yearLate'])
    else:
        datering = artobject['dating']['year']
    kleuren = artobject['colors']      # list object, mogelijk leeg
    if kleuren:
        kleurenlijst = ''
        for kleur in kleuren:
            kleurenlijst += '<span class="label" style="background:%s"></span>' % (kleur,)
    else:
        kleurenlijst = 'Geen informatie'
    omschrijving = artobject['description']
    return (titel, afbeelding, titel, maker, collectie, datering, kleurenlijst, omschrijving)


objectpage = maak_objectpage()

if objectpage:
    paginabron = templatetext % objectpage

if paginabron:
    f = open('object.html', 'w')
    f.write(paginabron)
    f.close()
