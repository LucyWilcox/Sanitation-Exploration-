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

counryList = []

for rowNumberText, rowText in enumerate(all_data_text):
    rowNumberNumbers = rowNumberText+1
    country = rowText[3]
    year = rowText[4]
    indicator = str( rowText[1] )
    code = str( rowText[0] )
    value = all_data_numbers[rowNumberNumbers][valueIndex]
    code = code.strip('\"')
    
    print 'country is: ', country

    if code == desiredCode:
        print 'Yeah!!!'
        #print country, indicator, year, value
        
        if not country in counryList:
            data.append( (country, indicator, [value], [year]) )
            counryList.append(country)
        else:
            print data[ counryList.index(country) ][2].append(value)
            data[ counryList.index(country) ][3].append(year)
    
    
        pprint.pprint( data )
