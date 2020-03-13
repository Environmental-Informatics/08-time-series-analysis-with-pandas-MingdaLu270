#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 15:00:57 2020

@author: lu270
"""

import pandas as pd
import numpy as np
from pandas import Series, DataFrame, Panel
import matplotlib.pyplot as plt

pd.set_option('display.max_rows',15)
print('version',pd.__version__)

ao=np.loadtxt('monthly.ao.index.b50.current.ascii.txt')
print(ao[0:2])
print(ao.shape)

## TS
dates=pd.date_range('1950-01',periods=ao.shape[0],freq="M")
print(dates)
print(dates.shape)

AO=Series(ao[:,2],index=dates)
print(AO)

AO.plot()
plt.title('Daily Atlantic Oscillation')
plt.xlabel('Dates')
plt.ylabel('Value')
plt.show()

AO['1980':'1990'].plot()
plt.show()

AO['1980-05':'1981-03'].plot()
plt.show()

print(AO[120])
print(AO['1960-01'])
print(AO['1960'])
print(AO[AO>0])

## DF
nao=np.loadtxt('norm.nao.monthly.b5001.current.ascii.txt')
dates_nao=pd.date_range('1950-01',periods=nao.shape[0],freq='M')
NAO=Series(nao[:,2],index=dates_nao)

print(NAO.index)

aonao=DataFrame({'AO':AO,'NAO':NAO})
aonao.plot(subplots=True)
plt.show()

print(aonao.head())
print(aonao['NAO'])
print(aonao.NAO)

aonao['Diff']=aonao['AO']-aonao['NAO']
print(aonao.head())

del aonao['Diff']
print(aonao.head())

print(aonao['1981-01':'1981-03'])

import datetime
aonao.loc[(aonao.AO>0)&(aonao.NAO<0)&(aonao.index>datetime.datetime(1980,1,1))&(aonao.index<datetime.datetime(1989,1,1)),'NAO'].plot(kind='barh')
plt.show()

## STATS
print('mean\n',aonao.mean())
print('max\n',aonao.max())
print('min\n',aonao.min())
print('mean1\n',aonao.mean(1))
print('decribe\n',aonao.describe())

## Resampling

AO_mm=AO.resample("A").mean()
AO_mm.plot(style='g--')
plt.show()

AO_mm=AO.resample("A").median()
AO_mm.plot()
plt.title('Annual Median Values for AO')
plt.xlabel('Dates')
plt.ylabel('Value')
plt.show()

AO_mm=AO.resample("3A").apply(np.max)
AO_mm.plot()
plt.show()

AO_mm=AO.resample("3A").apply(['mean',np.min,np.max])
AO_mm['1900':'2020'].plot(subplots=True)
AO_mm['1900':'2020'].plot()
plt.show()

print(AO_mm)

## Rolling Stats
aonao.rolling(window=12,center=False).mean().plot(style='-g')
plt.title('Rolling Mean afor Both AO and NAO')
plt.xlabel('Dates')
plt.ylabel('Value')
plt.show()

aonao.AO.rolling(window=120).corr(other=aonao.NAO).plot(style='-g')
plt.show()

print(aonao.corr())





