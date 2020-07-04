# Get definitions of each word in the supplied word list 'words'
from GetWords import *
from bs4 import BeautifulSoup
import urllib3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

urls = ["https://www.theguardian.com/international", "https://www.newyorker.com"]

#words, talley = getwords(urls, 5) # Just for testing, later  a seperate program will call both getdefs and getwords

defs = []
transliterations = []

def getdef(words):
	search = 'https://translate.google.com/#en/kn/'
	driver = webdriver.Firefox()
	for word in words:
		defurl = search + word
		driver.get(defurl)
		time.sleep(0.5)
		content = driver.page_source.encode('utf-8').strip()

		#r = requests.get(defurl)
		#r.encoding = 'utf-8'
		#text = r.text
		#soup_a = BeautifulSoup(text.encode('utf-8','ignore'), 'html.parser')
		#a = gethtml(defurl)

		soup_a = BeautifulSoup(content, 'html.parser')

		meanings = soup_a.find('span', {'class':'gt-baf-cell gt-baf-word-clickable'})
		if type(meanings) == 'NoneType':
			above = soup_a.find('span', {'class':'tlid-translation translation'})
			meanings = above.find('span',{'class':''})
			continue

		transliteration = soup_a.findAll('div', {'class':'tlid-transliteration-content transliteration-content full'})

		#meanings = driver.find_element_by_class_name('gt-baf-cell gt-baf-word-clickable')
		defs.append(meanings.text)
		transliterations.append(transliteration[1].text)
	
	driver.close()
	return defs, transliterations




