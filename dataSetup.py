# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 15:13:27 2015

@author: hdavis
"""

print 'Running code!'

##import pandas as pd
import numpy as np
import pickle
#download data from: http://databank.worldbank.org/data/download/WDI_csv.zip
  
print 'libraries loaded!'

print '\n Loading text data!'
#Open data into numpy arrays:
wdi_all_data_text = np.recfromcsv('WDI_Data2.csv', delimiter=',',usecols=np.arange(0,60)) #genfromtxt 
print 'Text data loaded.'
wdi_all_data_numbers = np.genfromtxt('WDI_Data2.csv', delimiter=',',usecols=np.arange(0,60))
print 'Number data loaded.'


#Save the resulting arrays:
np.save("BulkData/wdi_all_data_text", wdi_all_data_text)
print 'Text data from WDI pickled!'
np.save("BulkData/wdi_all_data_numbers", wdi_all_data_numbers )
print 'Number data from WDI pickled'
