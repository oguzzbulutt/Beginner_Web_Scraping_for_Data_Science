# import requests

# # url= 'http://www.webscrapingfordatascience.com/paramhttp/?query=test'
# url= 'http://www.webscrapingfordatascience.com/paramhttp/?query=a query with spaces'
# r=requests.get(url)

# print(r.request.url)
# print(r.text)

########################################################################################

# import requests

# url= 'http://www.webscrapingfordatascience.com/paramhttp/?query=a query with spaces'
# r=requests.get(url)

# print(r.request.url)#The spaces printed as %20 
# print(r.text)

# # I will use method url-lib.parse function for solve this problem

#########################################################################################

# import requests
# from urllib.parse import quote, quote_plus

# raw_string= 'a query with /, spaces and?&'

# print(quote(raw_string))# The spaces getted as %20 and other /?& operators get their numerical equal. It allows /
# print(quote_plus(raw_string))# The spaces getted + and other stuff get their numerical equal. It do not allow / and change it

#########################################################################################

# import requests
# from urllib.parse import quote, quote_plus

# raw_string= 'a query with /, spcaes and?&'
# url='http://www.webscrapingfordatascience.com/paramhttp/?query='

# print('Using quote:')
# #Nothing is safe, not even '/' characters, so encode everything
# r=requests.get(url+quote(raw_string, safe=''))

# print(r.url)
# print(r.next)

# print('\nUsing quote_plus:')
# r=requests.get(url+quote_plus(raw_string))

# print(r.url)
# print(r.next)

#######################################################################################

# import requests

# url='http://www.webscrapingfordatascience.com/paramhttp/'

# parameters={
#     'query': 'a query with /, spaces and?&'
# }

# r=requests.get(url,params=parameters)

# print(r.url)
# print(r.text)

#######################################################################################

import requests
from urllib.parse import unquote

class NonEncodedSession(requests.Session):#This function allow program to get url direty and clear.
    def send(self, *a, **kw):
        a[0].url= unquote(a[0].url)
        return requests.Session.send(self, *a, **kw)

my_requests=NonEncodedSession()
url= 'http://www.example.com/?spaces  |pipe'
r=my_requests.get(url)

print(r.url)

#######################################################################################
