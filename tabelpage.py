#!/usr/bin/env python3

from client import request_stukken, perpagina, pagina
from tabeltemplate import templatetext

stukken = request_stukken()

paginabron = ''
aantal = stukken['count']
responsetijd = stukken['elapsedMilliseconds']


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
            print(stuk['id'])    #dev
            tablerow = row % (stuk['title'], stuk['principalOrFirstMaker'], stuk['objectNumber'], stuk['links']['web'])

            htmltabel += tablerow

        htmltabel += '</tbody></table>'
        return htmltabel
    else:
        print('Geen stukken gevonden')


tabel = maak_tabel()

if tabel:
    paginabron = templatetext % (aantal, perpagina, pagina, responsetijd, tabel)

if paginabron:
    f = open('tabel.html', 'w')
    f.write(paginabron)
    f.close()
