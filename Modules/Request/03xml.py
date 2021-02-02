import requests

r=requests.get('https://steamcommunity.com/id/dingo060899/')
print(r.text)
with open('steamdingo.html','w',encoding='utf-8') as f:
    f.write(r.text)