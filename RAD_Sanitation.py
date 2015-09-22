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
	if len(data1) != len(data2):
		print 'ERROR!!!! RUN ourCountries() FIRST!!!'

	data1C = []; data2C = []; years = []

	for index, value in enumerate(data1):

		if data1[index][0] != data2[index][0]:
			print 'ERROR!!!! RUN ourCountries() FIRST!!!'

		for index2, year in enumerate(data1[3]):
			if data1[index][3][index2] in data2[index][3]:
				indexDataD2List = data2[index][3].index(data1[index][3][index2])
				data1C.append( data1[index][2][index2] )
				data2C.append( data2[index][2][indexDataD2List] )
				years.append( data1[index][3][index2] )

	return data1C, data2C, years

