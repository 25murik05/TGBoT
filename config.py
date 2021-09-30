import json
import requests

TOKEN = '2040207489:AAGCLhlnv2F7YwelBXoq8tPgt6_xWjcblhs'

value = {}

sait = 'http://api.exchangeratesapi.io/v1/latest?access_key=ca7ca6206374124554db12650fdb12be&format=1'
html = requests.get(sait).content
f = json.loads(html)
for _ in f:
    if _ == 'rates':
        value = f[_]
