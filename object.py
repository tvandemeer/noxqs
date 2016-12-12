#!/usr/bin/env python3

templatetext = '''<!doctype html>
<html class="no-js" lang="en">
    <head>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/foundation/6.2.4-rc2/foundation.min.css" />
        <style>
            body {
                background: url(http://lh5.ggpht.com/H-KfOaNgW2an_g0kODWKua5BELckMTr7zauQZCbnOZ69fyNlr67uavKaDmvSawg8j6TB88abmtAjNbcMjbOdU94zuzM=s0) no-repeat center fixed;
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
                <div class="callout" style="background-color:rgba(255,255,255,0.2);border-radius:6px;margin-bottom:10px">
                    <h4>Naam Werk</h4>
                    <h6>Naam Kunstenaar</h6>
                </div>
            </div>
            <div class="columns large-4 large-offset-2">
                <div class="callout float-right" style="background-color:rgba(255,255,255,0.2);border-radius:6px">
                    <h4>Details</h4>
                    <h6><strong>Collectie</strong></h6>
                    <h6><strong>Datering: van / tot</strong></h6>
                    <div style="padding:20px 0 20px 0">
                        <h6><strong>Primaire kleuren:</strong></h6>
                        <span class="label" style="background:#ff6600"></span>
                        <span class="label"></span>
                        <span class="label"></span>
                        <span class="label"></span>
                        <span class="label"></span>
                        <span class="label"></span>
                        <span class="label"></span>
                    </div>
                    <h6><strong>Omschrijving</strong></h6>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam pretium fermentum dolor quis semper. Sed vel porttitor leo, a faucibus sapien. Ut ut lobortis turpis. Quisque ac ex malesuada, pellentesque purus nec, pellentesque felis. Suspendisse potenti. Nunc posuere lacus eget massa efficitur rutrum. Aliquam sed vehicula nisl. Quisque ut diam ullamcorper, sagittis dolor sit amet, molestie metus. Aenean viverra massa eu purus varius, et lacinia ipsum cursus. Nam vestibulum mi a suscipit tincidunt. Etiam eu aliquet magna. Integer vitae ullamcorper purus, non aliquet felis. Mauris laoreet ultricies dapibus. Praesent vehicula eros ligula, ac tincidunt neque sollicitudin vel. Ut bibendum velit.</p>
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
