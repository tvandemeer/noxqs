#!/usr/bin/env python3

templatetext = '''<!doctype html>
<html class="no-js" lang="en">
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Stukkentabel</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/foundation/6.2.4-rc2/foundation.min.css" />
  </head>
  <body>

  <div class='row'>
    <div class='callout secondary'>
        <ul>
            <li>Aantal objecten: %d</li>
            <li>Per pagina: %d</li>
            <li>Pagina: %d</li>
            <li>Responsetijd: %d ms</li>
        </ul>
    </div>
  </div>

  <div class='row'>
    <div class='columns'>
    %s
    </div>
  </div>

  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
  <script src="https://cdn.jsdelivr.net/foundation/6.2.4/foundation.min.js"></script>
  <script>
      $(document).foundation();
  </script>

  </body>
</html>
'''
