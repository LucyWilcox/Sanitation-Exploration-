# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 15:13:27 2015

@author: hdavis
"""

##import pandas as pd
import numpy as np
import pickle
#download data from: http://databank.worldbank.org/data/download/WDI_csv.zip
#dtype=('i4,f4,a10')

# wdi_all_data_numbers = np.genfromtxt('WDI_Data.csv', 
# 	delimiter=',', 
# 	dtype=('i4,f4,a52,float32,int8'), 
# 	usecols=np.arange(0,60))

# print wdi_all_data_numbers



# wdi_data = []

# data_file = open("WDI_Data.csv", "r")
# try:
#     while True:    
#         wdi_data.append(data_file.readline())
# except: 
#     pass

# print wdi_data[1]

# for index, __ in enumerate(wdi_data):
#     wdi_data[index] = wdi_data[index].split(',')

# pickle.dump(wdi_data, open( "wdi_all_data.p", "wb" ) )    

wdi_all_data_text = np.recfromcsv('WDI_Data.csv', delimiter=',',usecols=np.arange(0,60)) #genfromtxt 

wdi_all_data_numbers = np.genfromtxt('WDI_Data.csv', delimiter=',',usecols=np.arange(0,60))

pickle.dump(wdi_all_data_text, open( "wdi_all_data_text.p", "wb" ) )
print 'Text data from WDI pickled!'
pickle.dump(wdi_all_data_numbers, open( "wdi_all_data_numbers.p", "wb" ) )
print 'Number data from WDI pickled'


#for i in range(len(wdi_all_data_numbers)):
    #for j in range(len(wdi_all_data_numbers[i])):
            #if wdi_all_data_numbers[i][j]=='nan':
                #wdi_all_data_numbers[i][j]=wdi_all_data_text[i][j]
                
                
#arrays = [np.array(map(int, line.split())) for line in open('WDI_Data.csv')]


#print wdi_all_data_numbers[0]
#print arrays[0]
#pickle.dump(wdi_all_data, open( "wdi_all_data.p", "wb" ) )
#print "Full WDI Data has been read in and saved to file!"



###Depricated Pandas stuff:

#data=pd.read_csv('WDI_Data.csv')#, 'Improved sanitation facilities (% of population with access)')
#data

#d2 = data.groupby('Indicator Name')
#print dir(d2)
#d2['Improved sanitation facilities (% of population with access)']