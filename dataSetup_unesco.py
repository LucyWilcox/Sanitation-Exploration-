# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 15:13:27 2015

@author: hdavis
"""

##import pandas as pd
import numpy as np
import pickle
#download data from: http://databank.worldbank.org/data/download/WDI_csv.zip
  

#Open data into numpy arrays:
all_data_text = np.recfromcsv('unesco_data.csv', delimiter=',',usecols=np.arange(0,8)) #genfromtxt 
print 'Text data loaded.'
all_data_numbers = np.genfromtxt('unesco_data.csv', delimiter=',',usecols=np.arange(0,8))
print 'Number data loaded.'


#Save the resulting arrays:
np.save("BulkData/unesco_all_data_text", all_data_text)
print 'Text data from UNESCO pickled!'
np.save("BulkData/unesco_all_data_numbers", all_data_numbers )
print 'Number data from UNESCO pickled'
