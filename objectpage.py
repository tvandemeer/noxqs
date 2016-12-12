#!/usr/bin/env python3

from client import object_info
from objecttemplate import templatetext

artobject = object_info()

def maak_objectpage():
    titel = artobject['title']
    maker = artobject['principalMakers'][0]['name']
    collectie = artobject['objectCollection'][0]
    if artobject['dating']['yearEarly'] != artobject['dating']['yearLate']:
        datering = '%s - %s' % (artobject['dating']['yearEarly'], artobject['dating']['yearLate'])
    else:
        datering = artobject['dating']['year']
    kleuren = artobject['colors']      # list object, mogelijk leeg
    omschrijving = artobject['description']


objectpage = maak_objectpage()

if objectpage:
    paginabron = templatetext % (objectpage,)

if paginabron:
    f = open('object.html', 'w')
    f.write(paginabron)
    f.close()
