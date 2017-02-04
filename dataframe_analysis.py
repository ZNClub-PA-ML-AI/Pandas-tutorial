# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 14:08:51 2017

@author: ZNevzz
"""
import pandas as pd

#web_stats = {'Day':[1,2,3,4,5,6],
#             'Visitors':[43,34,65,56,29,76],
#             'Bounce Rate':[65,67,78,65,45,52]}
#
#df = pd.DataFrame(web_stats)
#
#print(df.head())
#print(df.tail())
#print(df.tail(2))
#df.set_index('Day', inplace=True)
#print(df.head())
#print(df['Visitors'])
#print(df[['Visitors','Bounce Rate']])
#

df1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])

#concat = pd.concat([df1,df2])
#print(concat)
#
#df4 = df1.append(df2)
#print(df4)
#
#df4 = df1.append(df3)
#print(df4)

#s = pd.Series([80,2,50], index=['HPI','Int_rate','US_GDP_Thousands'])
#df4 = df1.append(s, ignore_index=True)
#print(df4)

df4 = pd.merge(df1,df3, on='HPI')
df4.set_index('HPI', inplace=True)
print(df4)


