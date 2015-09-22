import numpy as np
import pickle
import math
import pprint

def ourCountries(fullData, ourCountryList):
	'''Take in the data from all countries and return a list with only the data from a 
	list of desired countries. 

	INPUT: 
		fullData: list of tuples which is all the data about the indicator.
		ourCountryList: list of strings where the strings are the countries used in WDI.
	OUTPUT: 
		listDesiredCountries: a list of the data from the user specified countries. '''
	#[(Country, indicator, [values],[years]), (Country, indicator, [values],[years]),...]
	listDesiredCountries=[]
	for data in fullData:
		if data[0] in ourCountryList:
			listDesiredCountries.append(data)
	return listDesiredCountries
