#!/usr/bin/env python3

from client import request_stukken
from tabeltemplate import templatetext

stukken = request_stukken()

paginabron = ''


def maak_tabel():
    htmltabel = '''<table>
                        <thead>
                            <tr>
                                <th>Titel</th>
                                <th>Link Extern</th>
                            </tr>
                        </thead>
                        <tbody>
                '''

    row = '''<tr><td>%s</td>
            <td><a href="%s">Info</a></td></tr>
          '''

    if stukken:
        for stuk in stukken:
            print(stuk['id'])    #dev
            tablerow = row % (stuk['title'], stuk['links']['web'])

            htmltabel += tablerow

        htmltabel += '</tbody></table>'
        return htmltabel
    else:
        print('Geen stukken gevonden')


tabel = maak_tabel()

if tabel:
    paginabron = templatetext % (tabel,)

if paginabron:
    f = open('tabel.html', 'w')
    f.write(paginabron)
    f.close()

