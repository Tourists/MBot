from bs4 import BeautifulSoup
from urllib.request import urlopen

def scrape_from_wiki(s):
	wiki = "https://en.wikipedia.org/wiki/"
	s = s.replace(" ","_")
	wiki = wiki+s
	print (wiki)
	url = urlopen(wiki)
	soup = BeautifulSoup(url,"lxml")
	right_table=soup.find('table', class_='infobox')
	count = 0
	for row in right_table.findAll("tr"):
		title = row.findAll('th')
		cells = row.findAll('td')
		if not count==0:
			print (title[0].find(text=True))
			print (cells[0].find(text=True))
		count = count+1

scrape_from_wiki("harold and kumar")