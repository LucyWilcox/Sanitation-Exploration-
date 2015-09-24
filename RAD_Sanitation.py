import numpy as np
import pickle
import math
import pprint

#[(Country, indicator, [values],[years]), (Country, indicator, [values],[years]),...]

def ourCountries(fullData, ourCountryList):
	'''Take in the data from all countries and return a list with only the data from a 
	list of desired countries. 

	INPUT: 
		fullData: list of tuples which is all the data about the indicator.
		ourCountryList: list of strings where the strings are the countries used in WDI.
	OUTPUT: 
		listDesiredCountries: a list of the data from the user specified countries. '''
	listDesiredCountries=[]
	for data in fullData:
		if data[0] in ourCountryList:
			listDesiredCountries.append(data)
	return listDesiredCountries

def yearCorrelate(data1,data2):
	''' '''
	#(Country, indicator, [values],[years])
	data1CList = []; data2CList = []; yearsList = []

	indexYear = 3
	indexValue = 2
	for d1index, year in enumerate(data1[indexYear]):
		if year in data2[indexYear]:
			currentD1Value = data1[indexValue][d1index]
			yearsList.append(year)
			data1CList.append(currentD1Value)
			data2CList.append( data2[indexValue][ data2[indexYear].index(year) ])

	return data1CList, data2CList, yearsList

