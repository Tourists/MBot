import urllib2
import bs4

wiki = "https://en.wikipedia.org/wiki/"
s = raw_input()
s = s.replace(" ","_")
wiki = wiki+s
print wiki
url = urllib2.urlopen(wiki)
from bs4 import BeautifulSoup
soup = BeautifulSoup(url,"lxml")
right_table=soup.find('table', class_='infobox')
count = 0
for row in right_table.findAll("tr"):
	title = row.findAll('th')
	cells = row.findAll('td')
	if not count==0:
		print title[0].find(text=True)
		print cells[0].find(text=True)
	count = count+1
	