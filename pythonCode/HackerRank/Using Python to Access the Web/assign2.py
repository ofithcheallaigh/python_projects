# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

list1 = list()
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# finalNum = range(1)

# What I need is every time we go through the loop, all url's are added to the
# list. The required url is then selected as the new url and we cycle the
# required amount of times.

# url =  'http://py4e-data.dr-chuck.net/known_by_Fikret.html'     # Initial test url
url =  'http://py4e-data.dr-chuck.net/known_by_Samanta.html'
# for num in finalNum:
# url =  'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
# url = input('Enter - ')
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')


# Does this need an outer loop? To bring in the new print and url?
# I would need to move the url from the inner loop to the outer one

# Retrieve all of the anchor tags
myNum = range(7)
for num in myNum:
    url = url
    html = urllib.request.urlopen(url, context=ctx).read()
    # html = urllib.request.urlopen(newURL, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        # print(tag.get('href', None))
        x = tag.get('href', None)
        list1.append(x)
        # print(list1[2])
    url = list1[17]
    list1 = []

# print(newURL)
# print('The original url type is - ', type(url))
# print('The new url type is - ',type(newURL))

# Endented to here will give me just 1 url
# print(list1[2])
print(url)

