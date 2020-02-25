# Title: df Contructor
# Author: Doug Hart
# Date Created: 2/25/2020
# Last Updated: 2/25/2020

import pandas as pd 
import numpy as np
import multiprocessing as mp
from functions import convert_panel

#reading in and restructuring my data to fit panel format
df = pd.read_csv('medsales.csv',header=None)
panel_ready = convert_panel(df,4)
dfpr = pd.DataFrame(panel_ready)

df2 = pd.read_csv('scount2.csv', header=None)
newsheet = convert_panel(df2,4)
dfpr2 = pd.DataFrame(newsheet)

df3 = pd.read_csv('med_cut.csv',header=None)
newsheet3 = convert_panel(df3,4)
dfpr4 = pd.DataFrame(newsheet3)

df5 = pd.read_csv('n_days.csv', header=None)
newsheet5 = convert_panel(df5,4)
dfpr5 = pd.DataFrame(newsheet5)

df6 = pd.read_csv('foreclosed.csv',header=None)
newsheet6 = convert_panel(df6,4)
dfpr6= pd.DataFrame(newsheet6)

df7 = pd.read_csv('raw_inv.csv',header=None)
newsheet7 = convert_panel(df7,4)
dfpr7 = pd.DataFrame(newsheet7)

df8 = pd.read_csv('new_listings.csv',header=None)
newsheet8 = convert_panel(df8,4)
dfpr8 = pd.DataFrame(newsheet8)

df9 = pd.read_csv('med_daily.csv',header=None)
newsheet9 = convert_panel(df9,4)
dfpr9 = pd.DataFrame(newsheet9)

#naming columns so that I can conveniently call them when merging
dfpr.rename(columns={0: 'date', 
                   1: 'id', 2: 'city', 3: 'state', 4: 'med_price' }, inplace=True)
dfpr2.rename(columns={0: 'date', 
                   1: 'id', 2: 'city', 3: 'state', 4: 'sale_count' }, inplace=True)
dfpr4.rename(columns={0: 'date', 
                   1: 'id', 2: 'city', 3: 'state', 4: 'med_price_cut' }, inplace=True)
dfpr5.rename(columns={0: 'date', 
                   1: 'id', 2: 'city', 3: 'state', 4: 'med_days_listed' }, inplace=True)
dfpr6.rename(columns={0: 'date', 
                   1: 'id', 2: 'city', 3: 'state', 4: 'percent_foreclosed' }, inplace=True)
dfpr7.rename(columns={0: 'date', 
                   1: 'id', 2: 'city', 3: 'state', 4: 'num_listed' }, inplace=True)
dfpr8.rename(columns={0: 'date', 
                   1: 'id', 2: 'city', 3: 'state', 4: 'new_listing_m' }, inplace=True)
dfpr9.rename(columns={0: 'date', 
                   1: 'id', 2: 'city', 3: 'state', 4: 'med_daily_inv' }, inplace=True)


#creating final use dataframe and merging columns into it
final = pd.merge(dfpr,dfpr2, on= ['date','id','city','state'], how = 'left')

final = pd.merge(final,dfpr4, on= ['date','id','city'], how = 'left')
final.shape

final.rename(columns = {'state_x':'perm_state'}, inplace = True)

final = pd.merge(final,dfpr5, on= ['date','id','city'], how = 'left')
final.shape
final = pd.merge(final,dfpr6, on= ['date','id','city'], how = 'left')
final.shape
final = pd.merge(final,dfpr7, on= ['date','id','city'], how = 'left')
final.shape
final = pd.merge(final,dfpr8, on= ['date','id','city'], how = 'left')
final.shape
final = pd.merge(final,dfpr9, on= ['date','id','city'], how = 'left')
final.shape

final.drop('state_y', inplace=True, axis = 1)
final.drop('state_x', inplace=True, axis = 1)

final.rename(columns = {'perm_state':'state'}, inplace = True)