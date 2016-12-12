#!/usr/bin/env python3

templatetext = '''<!doctype html>
<html class="no-js" lang="en">
    <head>
        <title>%s</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/foundation/6.2.4-rc2/foundation.min.css" />
        <style>
            body {
                background: url(%s) no-repeat center fixed;
                background-size: cover;
            }
            .label {
                width: 30px;
                height: 30px;
            }
    </style>
    </head>
    <body>

        <div class="row" style="padding-top:20px">
            <div class="columns large-6">
                <div class="callout" style="background-color:rgba(255,255,255,0.6);border-radius:6px;margin-bottom:10px">
                    <h4>%s</h4>
                    <h6>%s</h6>
                </div>
            </div>
            <div class="columns large-4 large-offset-2">
                <div class="callout float-right" style="background-color:rgba(255,255,255,0.6);border-radius:6px">
                    <h4>Details</h4>
                    <h6><strong>Collectie: </strong>%s</h6>
                    <h6><strong>Datering: </strong>%s</h6>
                    <div style="padding:20px 0 20px 0">
                        <h6><strong>Primaire kleuren</strong></h6>
                        %s
                    </div>
                    <h6><strong>Omschrijving</strong></h6>
                    <p>%s</p>
                </div>
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
