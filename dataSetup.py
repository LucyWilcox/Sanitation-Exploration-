# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 15:13:27 2015

@author: hdavis
"""

import pandas as pd
import numpy as np
#download data from: http://databank.worldbank.org/data/download/WDI_csv.zip

data=pd.read_csv('WDI_Data.csv')

print data.groupby('Indicator Name')