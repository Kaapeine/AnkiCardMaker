# The getwords(urls, i) function returns the 'i' most common words from a list of urls passed as the first argument. 

from bs4 import BeautifulSoup
import urllib3
import pandas as pd
import requests

gwordlist = {} # Keys = words, Values = tallies ## This is the global wordlist
empty = {} # Empty placeholder dictonary

def gethtml(url): # Returns the html file of the url
	http = urllib3.PoolManager()
	html = http.request('GET', url)
	return html

def getbodytext(url): # Returns the raw text of the html file 
	a = gethtml(url)
	soup_a = BeautifulSoup(a.data, 'html.parser')
	text_a = soup_a.get_text()
	return text_a

def addtodict(text, dict): # For each string (raw text), it adds words to the dictonary
	list = text.split()
	for a in list:
		if a in dict:
			dict[a] = dict[a] + 1
		else:
			dict[a] = 1
	return dict

def getrepeatwords(dict, i, j): # To be used at the end, to sort the global dictonary and get the 'i:j' range of words
	a = []
	list1 = [] 
	for key in dict.keys(): 
		list1.append(key) 
		
	for x in dict.values():
		a.append(x) # a is a list with the talleys
	
	a, list1 = (list(t) for t in zip(*sorted(zip(a, list1)))) # ascending order
	list1.reverse()
	a.reverse()
	return list1[i:j], a[i:j]

def getmainwordlist(wordlist, urls, i, j): # Args are an empty dictionary and a list of urls
	for url in urls:
		text = getbodytext(url)
		addtodict(text, wordlist)

	words, talley = getrepeatwords(wordlist, i, j)
	return words, talley

def getwords(urls, i, j):
	empty = {}
	# i = 5 # 2nd Parameter: Most 'i' repeated words to be selected

	#************* Step-wise, now part of getmainwordlist() **************#

	# text = getbodytext("https://www.theguardian.com/international")     # text = 'To concatenate, or combine, two two strings strings you can use the + operator.'
	# dict1 = addtodict(text, gwordlist)
	# words, talley = getrepeatwords(dict1, i)
	# print(words)

	# counts = pd.DataFrame({'Words':words, 'Tallies':talley})
	# counts.to_csv('counts.csv', index=False, encoding='utf-8')

	#*********************************************************************#
	
	words, talley = getmainwordlist(empty, urls, i, j)
	return words, talley
	