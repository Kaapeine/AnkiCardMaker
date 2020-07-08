from GetWords import getwords
from GetDefs import getdef
import pandas as pd

if __name__=="__main__":
	urls = ["https://www.theguardian.com/international", "https://www.newyorker.com"]
	words, talley = getwords(urls, 15, 30)
	print(words, talley)

	#words = ['–', 'that', 'Covid-19'] #, 'says', 'as'] #, 'New', 'Guardian', 'not', 'it', 'his', 'has', 'WHO', 'have']
	print(words)

	defs,lits = getdef(words)
	#print(defs)
	#print(lits)

	dictionary = pd.DataFrame({'Words':words, 'Meanings':defs, 'Transliterations':lits})
	dictionary.to_csv('dict.csv', index=False, encoding='utf-8-sig')


	
