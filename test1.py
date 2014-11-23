# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 15:42:34 2014

@author: stn821
"""

import pandas as pd

data=pd.read_csv('static/specs_new.csv')
data['Style']=data['Style'].map(str.strip)
data['StyleOutput']=data['StyleOutput'].map(str.strip)
data['Preference']=data['Preference'].map(str.strip)

data_root=pd.read_csv('static/root.csv')
data_root=data_root.drop('linksImages',axis=1)
merged=data.merge(data_root,on='Id')
print merged.tail()
merged.to_csv('static/specs.csv')
df_filtered = merged[merged.StyleOutput == 'full']
print df_filtered.tail()