import requests
import lxml.html
import json
link = "https://textdoc.co/wfvnPNrVdsqIl6ig"
response = requests.get(link)
tree = lxml.html.fromstring(response.text)
element = tree.xpath('//*[@id="txt-doc"]/text()')[0]
cikti = json.loads(element)
