# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 04:26:50 2018

@author: kkrao
"""

import os
import pandas as pd
from dirs import dir_data

os.chdir(dir_data)
df = pd.DataFrame()

for file in os.listdir('fuel_moisture/raw_10-16-2018'):
    df = df.append([pd.read_table('fuel_moisture/raw_10-16-2018/'+file)], ignore_index = True)
df.drop('Unnamed: 7', axis = 1, inplace = True)
df.columns = df.columns.str.lower()
df.to_pickle('vwc_10-16-2018')
df.drop_duplicates(subset = 'site').drop(['fuel','percent','date'], axis = 1).to_csv('fuel_moisture/site_info_query_10-16-2018.csv')
