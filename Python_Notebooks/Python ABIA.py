# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 18:30:58 2019

@author: shane
"""

import pandas as pd


abia = pd.read_csv('C:/Users/shane/OneDrive/Documents/STA380 Scott/data/ABIA.csv')

month_arrival_avg=abia.groupby(['UniqueCarrier','Month'])['ArrDelay'].agg('mean').reset_index()
month_dep_avg=abia.groupby(['UniqueCarrier','Month'])['DepDelay'].agg('mean').reset_index()

month_arrival_avg.to_csv('Month Arrival Avg.csv', index=True)
month_dep_avg.to_csv('Month Departure Avg.csv', index=True)
