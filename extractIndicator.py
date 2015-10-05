import numpy as np
import pickle
import math
import matplotlib.pyplot as plt
import pprint

##Load pickled data files. If these aren't present, run dataSetup.py
wdi_all_data_numbers = pickle.load( open( "wdi_all_data_numbers.p", "rb" ) )
print 'Loaded number data!'
wdi_all_data_text = pickle.load( open( "wdi_all_data_text.p", "rb" ) )
print 'Loaded text data'


##Cull through the data and pull out the data for a desired indicator:
##ImprovedSan format is: [(Country, indicator, [values],[years]), (Country, indicator, [values],[years]),...]

ImprovedSan=[]

for listDataNum, __ in enumerate(wdi_all_data_text):
	#print wdi_all_data_text[listDataNum][3]
	if (wdi_all_data_text[listDataNum][3]=='SE.SEC.ENRR') or (wdi_all_data_text[listDataNum][4]=='SE.SEC.ENRR'):
		print 'hi!'
		ImprovedSanVals=[]
		ImprovedSanYears=[]

		for index, value in enumerate(wdi_all_data_numbers[listDataNum][3:]):
			if not math.isnan(value):
				ImprovedSanVals.append(value)
				ImprovedSanYears.append(1960+index)

		ImprovedSan.append( (wdi_all_data_text[listDataNum][0], wdi_all_data_text[listDataNum][2], ImprovedSanVals, ImprovedSanYears) )


pprint.pprint(ImprovedSan)

pickle.dump(ImprovedSan, open( "dataPickles/grossSecondarySchoolEnrolment.p", "wb" ) )
print 'Processed data pickled!'