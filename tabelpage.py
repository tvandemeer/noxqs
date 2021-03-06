#!/usr/bin/env python3

import pdb # python debugger

from client import request_stukken, pagina
from tabeltemplate import templatetext
from math import ceil

# Voor uitgebreidere ondersteuning cli argumenten
import argparse
from urllib.parse import urlparse, parse_qs

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', help='url van een api endpoint (plaats de url tussen aanhalingstekens!)')
#parser.add_argument('-k', '--key', help='api key')
#parser.add_argument('-f', '--format', help='response type (xml/json/jsonp)')
#parser.add_argument('-t', '--type', help='object type')
#parser.add_argument('-i', '--image', help='afbeelding beschikbaar (True/False)')
#parser.add_argument('-p', '--piecestop', help='topstukken (True/False)')
#parser.add_argument('-b', '--bladzijde', help='index van pagina met resultaten')
#parser.add_argument('-a', '--aantal', help='aantal resultaten per pagina')
args = parser.parse_args()

pdb.set_trace()

query = {}
perpagina = 20

if args.url:
    query = parse_qs(urlparse(args.url).query)

stukken = request_stukken(query, perpagina)

paginabron = ''
aantal = stukken['count']
paginas = ceil(aantal/perpagina) # WELKE WAARDE PERPAGINA???


def maak_tabel():
    htmltabel = '''<table>
                        <thead>
                            <tr>
                                <th>Titel</th>
                                <th>Maker</th>
                                <th>Objectnummer</th>
                                <th>Link Extern</th>
                            </tr>
                        </thead>
                        <tbody>
                '''

    row = '''<tr><td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td><a href="%s">Info</a></td></tr>
          '''

    if stukken:
        for stuk in stukken['artObjects']:
            tablerow = row % (stuk['title'], stuk['principalOrFirstMaker'], stuk['objectNumber'], stuk['links']['web'])

            htmltabel += tablerow

        htmltabel += '</tbody></table>'
        return htmltabel
    else:
        print('Geen stukken gevonden')


tabel = maak_tabel()

if tabel:
    print(str(perpagina) + ' tabelpage') #DEBUG
    paginabron = templatetext % (aantal, perpagina, pagina, paginas, tabel)

if paginabron:
    f = open('tabel.html', 'w')
    f.write(paginabron)
    f.close()

