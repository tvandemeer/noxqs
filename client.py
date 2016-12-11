#!/usr/bin/env python3

import requests

# argumenten
apikey = '14OGzuak'
resptype = 'json'
soort = 'schilderij'
afbeelding = 'True'     # Alleen resultaten met afbeelding
topstukken = 'True'
aantal = 20     # Aantal resultaten per pagina


def request_stukken():

# api endpoint voor topstukken uit collectie schilderijen
    col = 'https://www.rijksmuseum.nl/api/nl/collection?key=%s&format=%s&type=%s&imgonly=%s&toppieces=%s&ps=%d' % (
        apikey, resptype, soort, afbeelding, topstukken, aantal)

    r = requests.get(col)
    if r.status_code == 200:
        stukken = r.json()['artObjects']
        return stukken
    else:
        print('Er is een fout opgetreden')


def object_info(object_id):

    # api endpoint voor object info
    obj = 'https://www.rijksmuseum.nl/api/nl/collection/%s?key=%s&format=json' % (object_id, apikey)

