#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 15:41:30 2020

@author: lu270
"""

import pandas as pd
import numpy as np
from pandas import Series, DataFrame, Panel
import matplotlib.pyplot as plt

## load data
data=pd.read_table('WabashRiver_DailyDischarge_20150317-20160324.txt',skiprows=26,sep=r"\s",usecols=[2,3,5],names=['datetime','time','discharge'])
print(data)

data['timestamp']=data['datetime']+' '+data['time']
data['datetime'] = pd.to_datetime(data['timestamp'])

data = data.drop(columns=['time','timestamp'])

data.index = data['datetime']

print(data)

Q=data.resample('D').mean()
print(Q)

Q.plot()
plt.title('Daily Average Streamflow')
plt.xlabel('Datetime')
plt.ylabel('Discharge (cfs)')
plt.savefig('Daily_Average_Discharge.pdf')
plt.show()

## Highest 10 plots
topQ = Q.nlargest(10,['discharge'])
x = pd.to_datetime(topQ.index)

hydrograph=Q.plot()
topten=plt.scatter(x,topQ.discharge,color='r',label='top 10 discharge data')
hydrograph.legend()
plt.title('Steamflow Data')
plt.xlabel('Datetime')
plt.ylabel('Dishcarge (cfs)')
plt.savefig('10_Days_with_Highest_Discharge.pdf')
plt.show()

## Monthly data
MQ=data.resample('M').mean()
MQ.plot()
plt.title('Monthly Average Streamflow')
plt.xlabel('Datetime')
plt.ylabel('Discharge (cfs)')
plt.savefig('Monthly_Average_Streamflow.pdf')
plt.show()










