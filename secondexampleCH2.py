import requests

# url='http://www.webscrapingfordatascience.com/basichttp/'
# url='https://tr.wikipedia.org/wiki/T%C3%BCrkiye' #My test for antoher website for check it response 
url='http://www.webscrapingfordatascience.com/paramhttp/?query=test'#2.4 Query string ex.
r=requests.get(url)


# print(r.status_code)# Check server for it giving response -->200

# print(r.reason)# Check server for it giving response -->OK

# print(r.headers)

# print(r.request)

# print(r.request.headers)

print(r.text)