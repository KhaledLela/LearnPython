# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

# ---- Layer 1 ---- Application/Code/instructions
# ---- Layer 2 ---- Intermediate layer between programming/kernel|OS
# Ex.1 read/write storage...
# with open("path") as handler:

# open TextIO
# FTP = 21
# SFTP = 22
# HTTP = 80
# HTTPS = 443
# host google.com
# google.com has address 142.251.143.206

# host data.pr4e.org
# data.pr4e.org has address 192.241.136.170


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
print(html)
# soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#     print(tag.get('href', None))

# for tag in tags:
#     # Look at the parts of a tag
#     print('TAG:', tag)
#     print('URL:', tag.get('href', None))
#     print('Contents:', tag.contents[0])
#     print('Attrs:', tag.attrs)

# Code: http://www.py4e.com/code3/urllinks.py