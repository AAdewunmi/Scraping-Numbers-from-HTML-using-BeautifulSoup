#Scraping Numbers from HTML using BeautifulSoup
#This program will use urllib to read the HTML from the data files below,
#and parse the data, extracting numbers and compute the sum of the numbers in the file.
# http://py4e-data.dr-chuck.net/comments_209569.html (Sum ends with 21)
#Data Format
#The file is a table of names and comment counts. You can ignore most of the data in the
#file except for lines like the following:

#<tr><td>Modu</td><td><span class="comments">90</span></td></tr>
#<tr><td>Kenzie</td><td><span class="comments">88</span></td></tr>
#<tr><td>Hubert</td><td><span class="comments">87</span></td></tr>
#You are to find all the <span> tags in the file and pull out the numbers from the tag
#and sum the numbers.

#Sample Execution

#$ python3 solution.py
#Enter - http://py4e-data.dr-chuck.net/comments_42.html
#Count 50
#Sum 2...

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

counter = 0
total = list()

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all span tags
tags = soup('span')

for tag in tags:
    total.append(int(tag.string))
    counter = counter + 1

print("Counter", counter)
print("Sum", sum(total))
