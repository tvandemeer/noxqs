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

        <div class="row">
            <div class="columns large-6 small-6">
                <button id="titelbutton" class="button secondary" type="button" style="opacity:0.5;border-radius:0 0 4px 4px"><strong>Titel &#8693;</strong></button>
            </div>
            <div class="columns large-6 small-6">
                <button id="detailsbutton" class="button secondary float-right" type="button" style="opacity:0.5;border-radius:0 0 4px 4px"><strong>Details &#8693;</strong></button>
            </div>
        </div>

        <div class="row">
            <div class="columns large-6">
                <div id="titelcallout" class="callout" style="background-color:rgba(255,255,255,0.5);border-radius:6px;margin-bottom:10px">
                    <h4>%s</h4>
                    <h6>%s</h6>
                </div>
            </div>
            <div class="columns large-4 large-offset-2">
                <div id="detailscallout" class="callout" style="background-color:rgba(255,255,255,0.5);border-radius:6px;display:none">
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

            $( "#titelbutton" ).click(function() {
                $( "#titelcallout" ).slideToggle( "slow" );
            });

            $( "#detailsbutton" ).click(function() {
                $( "#detailscallout" ).slideToggle( "slow" );
            });
        </script>
    </body>
</html>
'''
