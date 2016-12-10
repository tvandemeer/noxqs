#!/usr/bin/env python3

import requests

# argumenten
apikey = '14OGzuak'
resptype = 'json'
soort = 'schilderij'
afbeelding = 'True'
topstukken = 'True'
aantal = 20

# api endpoint voor topstukken uit collectie schilderijen
endpoint = 'https://www.rijksmuseum.nl/api/nl/collection?key=%s&format=%s&type=%s&imgonly=%s&toppieces=%s&ps=%d' % (apikey, resptype, soort, afbeelding, topstukken, aantal)

# api endpoint voor object info
obj = 'https://www.rijksmuseum.nl/api/nl/collection/%s?key=%s&format=json'


def request_stukken():
    r = requests.get(endpoint)
    if r.status_code == 200:
        stukken = r.json()['artObjects']
        return stukken
    else:
        print('Er is een fout opgetreden')


def object_info():
    pass

