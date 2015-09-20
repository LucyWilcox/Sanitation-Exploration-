# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 15:13:27 2015

@author: hdavis
"""

##import pandas as pd
import numpy as np
import pickle
#download data from: http://databank.worldbank.org/data/download/WDI_csv.zip

wdi_all_data = np.genfromtxt('WDI_Data.csv', delimiter=',',usecols=np.arange(0,60))

pickle.dump(wdi_all_data, open( "wdi_all_data.p", "wb" ) )
print "Full WDI Data has been read in and saved to file!"



###Depricated Pandas stuff:

#data=pd.read_csv('WDI_Data.csv')#, 'Improved sanitation facilities (% of population with access)')
#data

#d2 = data.groupby('Indicator Name')
#print dir(d2)
#d2['Improved sanitation facilities (% of population with access)']