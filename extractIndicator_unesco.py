import numpy as np
import pickle
import math
import matplotlib.pyplot as plt
import pprint

desiredIndicator = 'Percentage of primary schools with no information on electricity (%)'
desiredCode = b'SCHBSP_2_PU_MIXTOIL'

##Load pickled data files. If these aren't present, run dataSetup.py
all_data_numbers = np.load('BulkData/unesco_all_data_numbers.npy')
print 'Loaded number data!'
all_data_text = np.load( "BulkData/unesco_all_data_text.npy" )
print 'Loaded text data'


# [(Country, indicator, [values],[years]), (Country, indicator, [values],[years]),...]

data = []
valueIndex = 6


for rowNumberText, rowText in enumerate(all_data_text):
    rowNumberNumbers = rowNumberText+1
    country = rowText[3]
    year = rowText[4]
    indicator = str( rowText[1] )
    code = str( rowText[0] )
    value = all_data_numbers[rowNumberNumbers][valueIndex]
#    value = str(code)
    print 'value is: ', code
    code = code.strip('\"')
    print code
    
    #if indicator == desiredIndicator:
    derivedTruth = True
    for value in  zip(code, desiredCode):
        #if value is not desiredCode[index]:
            #derivedTruth = False
            #print 'FAIL!!!'
        print value
    if code == desiredCode:
        print 'Yeah!!!'
        #print country, indicator, year, value
        data.append( (country, indicator, value, year) )
    
    
pprint.pprint( data )
