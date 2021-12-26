# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file


from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
# url = 'http://py4e-data.dr-chuck.net/comments_42.html'
# url = 'http://www.dr-chuck.com'
url = 'http://py4e-data.dr-chuck.net/comments_13213.html'
html = urlopen(url, context=ctx).read()

# html.parser is the HTML parser included in the standard Python 3 library.
# information on other HTML parsers is here:
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
# soup = BeautifulSoup(html, "html.parser")
# print(soup)

soup = BeautifulSoup(html, "html.parser")

data2 = BeautifulSoup(html,"lxml")
mySum = sum(int(s.text) for s in  data2.select("span.comments"))
print(mySum)

