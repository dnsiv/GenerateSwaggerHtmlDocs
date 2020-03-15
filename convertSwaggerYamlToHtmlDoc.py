#!/usr/bin/python
"""
Usage:    python convertSwaggerYamlToHtmlDoc.py < /path/to/api.yaml > api.html
"""

import yaml, json, sys, glob, os

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Swagger UI</title>
  <link rel="stylesheet" type="text/css" href="lib/swagger-ui.css" >

  <style>
    html
    {
      box-sizing: border-box;
      overflow: -moz-scrollbars-vertical;
      overflow-y: scroll;
    }
    *,
    *:before,
    *:after
    {
      box-sizing: inherit;
    }

    body {
      margin:0;
      background: #fafafa;
    }
  </style>
</head>

<body>
<div id="swagger-ui"></div>
<script src="lib/swagger-ui-bundle.js"> </script>
<script src="lib/swagger-ui-standalone-preset.js"> </script>
<script>
window.onload = function() {
  var specs = %s;

  // Build a system
  const ui = SwaggerUIBundle({
    spec: specs,
    dom_id: '#swagger-ui',
    deepLinking: true,
    presets: [
      SwaggerUIBundle.presets.apis,
      SwaggerUIStandalonePreset
    ],
    plugins: [
      SwaggerUIBundle.plugins.DownloadUrl
    ],
    layout: "StandaloneLayout"
  })
  window.ui = ui;

  var elements = document.getElementsByClassName("download-url-wrapper");
    while(elements.length > 0){
    elements[0].parentNode.removeChild(elements[0]);
    }
}
</script>
</body>
</html>
"""


#iterate over all .yaml-files
for filepath in glob.iglob('src/*.yaml'):
    filename = os.path.basename(filepath)

    #load yaml file and convert to json
    file_json  = open(filepath, "r")
    spec = json.dumps(yaml.load(file_json, Loader=yaml.FullLoader))

    #create targetfile 
    file_obj  = open("targets/"+filename[0:-4]+"html", "w")
    file_obj.write(TEMPLATE % spec )