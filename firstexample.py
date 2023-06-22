import requests

url='http://www.webscrapingfordatascience.com/basichttp/'
r=requests.get(url)

print(r.status_code)

print(r.text)