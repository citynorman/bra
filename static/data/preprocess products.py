# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 15:42:34 2014

@author: stn821
"""

import pandas as pd

data=pd.read_csv('specs_new.csv')
data['Style']=data['Style'].map(str.strip)
data['StyleOutput']=data['StyleOutput'].map(str.strip)
data['Preference']=data['Preference'].map(str.strip)

data_root=pd.read_csv('root.csv')
data_root=data_root.drop('linksImages',axis=1)
merged=data.merge(data_root,on='Id')
#print merged.tail()
#merged.to_csv('specs.csv')

df_filtered = merged[merged.StyleOutput == 'balconette']
print df_filtered.tail()
print df_filtered.to_dict('records')