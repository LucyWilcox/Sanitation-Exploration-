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
	if wdi_all_data_text[listDataNum][3]=='SH.STA.ACSN':
		ImprovedSanVals=[]
		ImprovedSanYears=[]

		for index, value in enumerate(wdi_all_data_numbers[listDataNum][3:]):
			if not math.isnan(value):
				ImprovedSanVals.append(value)
				ImprovedSanYears.append(1960+index)

		ImprovedSan.append( (wdi_all_data_text[listDataNum][0], wdi_all_data_text[listDataNum][2], ImprovedSanVals, ImprovedSanYears) )
		#print 'Years =', ImprovedSanYears

print 'Culled through data. Now plotting!'


for dataSet in ImprovedSan:
	#print 'Years 2 = ', dataSet[3]
	#print 'indicator: ', dataSet[1]

	plt.plot(dataSet[3], dataSet[2], label=dataSet[0])

plt.show()

pprint.pprint(ImprovedSan)

