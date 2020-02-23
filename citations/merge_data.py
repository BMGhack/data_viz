# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 20:26:12 2020

@author: Tim
"""

import pandas as pd
from os import listdir
from os.path import isfile, join


datafiles = [f for f in listdir('data') if isfile(join('data', f)) and f.endswith('.csv')]
# Note: up to i = 6, datafiles[i] is CSV, then becomes xlsx
columns = []
common_columns = []
for i in range(len(datafiles)):    
    df = pd.read_csv('data/' + datafiles[i])
    columns += list(df.columns)
    common_columns.append(set(df.columns))
    
all_columns = set(columns)
common_columns = set.intersection(*common_columns)
# These are the common column names across all datasets. 
# Note that this does not mean the column doesn't exist.
# In fact, it seems it's more that the column name was changed at some point.
# Nevertheless, this will cause problems when merging the datasets. 
print(common_columns)