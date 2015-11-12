import numpy as np
import pickle
import math
import matplotlib.pyplot as plt
import pprint

desiredIndicator = 'Percentage of lower secondary schools with single-sex toilets (%)'
desiredCode = b'SCHBSP_2_PU_WSTOIL'

set_nan_to_zero = True

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
    
    ## Grab out/unpack fields:
    rowNumberNumbers = rowNumberText+1
    country = rowText[3]
    year = rowText[4]
    indicator = str( rowText[1] )
    code = str( rowText[0] )
    value = all_data_numbers[rowNumberNumbers][valueIndex]
    
    print type(value)
    
    ## Make the number fields an actual number
    try:
        year = int(year.strip('\"') )
    except:
        print 'Problem  with: ', year
    
    ## Remove quotation marks from front and back of string
    code = code.strip('\"')
    country = country.strip('\"')
    

    
    ## Only write the data for the indicator we want: 
    if code == desiredCode: 
    
        ## If specified, set NaN values to zero:
        if ( (set_nan_to_zero==True) and math.isnan(value) ):
            value=0
     
        ## Add the country to the data structure if it isn't there
        if not country in counryList:
            data.append( (country, indicator, [value], [year]) )
            counryList.append(country)
        ## Update country data lists if they already present
        else:
            data[ counryList.index(country) ][2].append(value)
            data[ counryList.index(country) ][3].append(year)
    
    
pprint.pprint( data )

pickle.dump(data, open( "dataPickles/unesco_"+desiredIndicator+".p" , "wb" ) )

##for entry in data:
###    print entry
##    if entry[0]=='Holy See':
##        print entry
