#! usr/bin/python

from bs4 import BeautifulSoup
import urllib2

coordinates = BeautifulSoup(urllib2.urlopen('http://www.sailwx.info/shiptrack/shipposition.phtml?call=wrn5495'))


for tr in coordinates.find_all ('tr')[3:]:
	tds = tr.find_all('td')
	print ("1: %s, 2:%s, 3: %s, 4:%s" %(tds[0].text, tds[1].text, tds[2].text, tds[3].text))
    

