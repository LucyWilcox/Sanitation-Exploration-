import numpy as np
import pickle
import math
import matplotlib.pyplot as plt
import pprint

##Load pickled data files. If these aren't present, run dataSetup.py
wdi_all_data_numbers = np.load('BulkData/wdi_all_data_numbers.npy')
print 'Loaded number data!'
wdi_all_data_text = np.load( "BulkData/wdi_all_data_text.npy" )
print 'Loaded text data'
#2524
print wdi_all_data_text[2524]


##Cull through the data and pull out the data for a desired indicator:
##ImprovedSan format is: [(Country, indicator, [values],[years]), (Country, indicator, [values],[years]),...]

ImprovedSan=[]
femaleSecondarySchoolEnrollmentCde = 'SE.SEC.ENRI.FE'
improvedSanitationCode = 'SH.STA.ACSN'

for listDataNum, __ in enumerate(wdi_all_data_text):
	#print wdi_all_data_text[listDataNum][3]
	if (wdi_all_data_text[listDataNum][3]== 'SE.SEC.ENRI.FE') or (wdi_all_data_text[listDataNum][4]== 'SE.SEC.ENRI.FE'):
		print wdi_all_data_numbers[listDataNum] # __, '\n'
		# print 'hi!'
		ImprovedSanVals=[]
		ImprovedSanYears=[]

		for index, value in enumerate(wdi_all_data_numbers[listDataNum+1][3:]):
			if not math.isnan(value):
				ImprovedSanVals.append(value)
				ImprovedSanYears.append(1960+index)

		ImprovedSan.append( (wdi_all_data_text[listDataNum][0], wdi_all_data_text[listDataNum][2], ImprovedSanVals, ImprovedSanYears) )

print 'Result is: '
pprint.pprint(ImprovedSan)

pickle.dump(ImprovedSan, open( "dataPickles/% Gross Female Secondary School Enrollment-C.p" , "wb" ) )
print 'Processed data pickled!'
