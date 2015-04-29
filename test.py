

from bs4 import BeautifulSoup
import geocoder
import json
import urllib2

coordinates = BeautifulSoup(urllib2.urlopen('http://www.sailwx.info/shiptrack/shipposition.phtml?call=wrn5495')

def get_data(coordinates):
    """scrape and save table"""
    with open ('AIS_Page.html', 'w') as AIS.encode:
    	for tr in coordinates.find_all ('tr')[3:]:
    		tds = tr.find_all('td')
    		AIS.write("1: %s, 2:%s, 3: %s, 4:%s" %(tds[0].text, tds[1].text, tds[2].text, tds[3].text))
    return 'print the'
# def get_geojson(result):
#     """map results"""

if __name__ == '__main__':
	get_data()

