#!/usr/bin/env python3

from client import object_info
from objecttemplate import templatetext
import sys

artobject = object_info(sys.argv[1])

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
    omschrijving = artobject['description']
    return (titel, afbeelding, titel, maker, collectie)


objectpage = maak_objectpage()

if objectpage:
    paginabron = templatetext % objectpage

if paginabron:
    f = open('object.html', 'w')
    f.write(paginabron)
    f.close()
