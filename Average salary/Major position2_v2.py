# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 14:02:28 2018

@author: ASZXJOHN
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data2014 = pd.read_csv('2014.csv', index_col='年度', parse_dates=True)
data2015 = pd.read_csv('2015.csv', index_col='年度', parse_dates=True)
data2016 = pd.read_csv('2016.csv', index_col='年度', parse_dates=True)
data2017 = pd.read_csv('2017.csv', index_col='年度', parse_dates=True)
data2014['年度']='2014'
data2015['年度']='2015'
data2016['年度']='2016'
data2017['年度']='2017'


allData=pd.concat([data2014, data2015, data2016, data2017], ignore_index=True)
'''
allData2=allData[allData.職類別.str.contains('程式設計師')]
allData3=allData2[(allData2.經常性薪資.str.contains('…')!=True) & (allData2.經常性薪資.str.contains('—')!=True)]
allData3['經常性薪資']=pd.to_numeric(allData3['經常性薪資'])
allData4=allData3.pivot_table(index='年度',columns=['職類別'],values=['經常性薪資'],aggfunc=np.mean)
'''
data2014 = data2014[data2014.職類別.str.contains('程式設計師')]
data2015 = data2015[data2015.職類別.str.contains('程式設計師')]
data2016 = data2016[data2016.職類別.str.contains('程式設計師')]
data2017 = data2017[data2017.職類別.str.contains('程式設計師')]
data2014 = data2014[(data2014.經常性薪資.str.contains('…')!=True) & (data2014.經常性薪資.str.contains('—')!=True)]
data2015 = data2015[(data2015.經常性薪資.str.contains('…')!=True) & (data2015.經常性薪資.str.contains('—')!=True)]
data2016 = data2016[(data2016.經常性薪資.str.contains('…')!=True) & (data2016.經常性薪資.str.contains('—')!=True)]
data2017 = data2017[(data2017.經常性薪資.str.contains('…')!=True) & (data2017.經常性薪資.str.contains('—')!=True)]
data2014['經常性薪資'] = pd.to_numeric(data2014['經常性薪資'])
data2015['經常性薪資'] = pd.to_numeric(data2015['經常性薪資'])
data2016['經常性薪資'] = pd.to_numeric(data2016['經常性薪資'])
data2017['經常性薪資'] = pd.to_numeric(data2017['經常性薪資'])
data2014_Aver = data2014['經常性薪資'].mean()
data2015_Aver = data2015['經常性薪資'].mean()
data2016_Aver = data2016['經常性薪資'].mean()
data2017_Aver = data2017['經常性薪資'].mean()


Average2014 = allData[(allData.經常性薪資.str.contains('…')!=True) & (allData.經常性薪資.str.contains('—')!=True) & (allData.年度.str.contains('2014')==True)]
Average2015 = allData[(allData.經常性薪資.str.contains('…')!=True) & (allData.經常性薪資.str.contains('—')!=True) & (allData.年度.str.contains('2015')==True)]
Average2016 = allData[(allData.經常性薪資.str.contains('…')!=True) & (allData.經常性薪資.str.contains('—')!=True) & (allData.年度.str.contains('2016')==True)]
Average2017 = allData[(allData.經常性薪資.str.contains('…')!=True) & (allData.經常性薪資.str.contains('—')!=True) & (allData.年度.str.contains('2017')==True)]
Average2014['經常性薪資']=pd.to_numeric(Average2014['經常性薪資'])
Average2015['經常性薪資']=pd.to_numeric(Average2015['經常性薪資'])
Average2016['經常性薪資']=pd.to_numeric(Average2016['經常性薪資'])
Average2017['經常性薪資']=pd.to_numeric(Average2017['經常性薪資'])

Average2014_ = Average2014['經常性薪資'].mean()
Average2015_ = Average2015['經常性薪資'].mean()
Average2016_ = Average2016['經常性薪資'].mean()
Average2017_ = Average2017['經常性薪資'].mean()


Average2014['標準差'] = np.power((Average2014['經常性薪資']-data2014_Aver),2)
Average2015['標準差'] = np.power((Average2015['經常性薪資']-data2015_Aver),2)
Average2016['標準差'] = np.power((Average2016['經常性薪資']-data2016_Aver),2)
Average2017['標準差'] = np.power((Average2017['經常性薪資']-data2017_Aver),2)
StandardDeviation2014= np.sqrt(np.sum(Average2014['標準差'])/len(Average2014['標準差']))
StandardDeviation2015= np.sqrt(np.sum(Average2015['標準差'])/len(Average2015['標準差']))
StandardDeviation2016= np.sqrt(np.sum(Average2016['標準差'])/len(Average2016['標準差']))
StandardDeviation2017= np.sqrt(np.sum(Average2017['標準差'])/len(Average2017['標準差']))

StandardDeviation = pd.DataFrame({'年度':['2014','2015','2016','2017']}) 
StandardDeviation.set_index('年度' , inplace=True)
StandardDeviation['工程師:經常性薪資平均']=[Average2014_,Average2015_,Average2016_,Average2017_]
StandardDeviation['標準差']=[StandardDeviation2014,StandardDeviation2015,StandardDeviation2016,StandardDeviation2017]
StandardDeviation['年度'] = ['2014','2015','2016','2017']
x1 = StandardDeviation['年度']
y1 = StandardDeviation['工程師:經常性薪資平均']
y2 = StandardDeviation['標準差']

plt.plot(x1,y1,'r-o')
plt.plot(x1,y2,'b-o')
plt.show()
plt.savefig('test.png')