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
		if word.isalpha() == False: # One problem: Words with a hiphen get filtered out
			defs.append(word)
			transliterations.append(word)
			continue

		defurl = search + word
		driver.get(defurl)
		time.sleep(0.5)
		content = driver.page_source.encode('utf-8').strip()

		soup_a = BeautifulSoup(content, 'html.parser')

		#meanings = soup_a.find('span', {'class':'gt-baf-cell gt-baf-word-clickable'})

		#if type(meanings) == 'NoneType':
		above = soup_a.find('span', {'class':'tlid-translation translation'})
		meanings = above.find('span',{'class':''})

		try:	
			defs.append(meanings.text)
		except AttributeError:
			defs.append(word)
			transliterations.append(word)

		transliteration = soup_a.findAll('div', {'class':'tlid-transliteration-content transliteration-content full'})
		transliterations.append(transliteration[1].text)

		#meanings = driver.find_element_by_class_name('gt-baf-cell gt-baf-word-clickable')
	
	driver.close()
	return defs, transliterations




