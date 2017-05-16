from __future__ import division
import datetime
import pandas as pd
import random
from random import randint
import numpy as np


def dummy_dataframe():
    """
    Input: Nothing, this function will create a dummy dataframe of orders of size 10
    return:
                sid  share side  price   re  unre  openposition  avgPrice
    2017-05-06    1     10    S     28    0     0           -10        28
    2017-05-07    1     10    B     52 -280     0             0         0
    2017-05-08    1     10    B     55    0     0            10        55
    2017-05-09    1     10    B     79    0   240            20        67
    2017-05-10    1     10    B     78    0   110            30        70
    2017-05-11    1     10    S     93  230     0            20        70
    2017-05-12    1     10    S     28 -420     0            10        70
    2017-05-13    1     10    B     55    0  -150            20        62
    2017-05-14    1     10    B     44    0  -180            30        56
    2017-05-15    1     10    B     69    0   130            40        59
    """
    todays_date = datetime.datetime.now().date()
    index = pd.date_range(todays_date-datetime.timedelta(10), periods=10, freq='D')
    columns = ['sid','share', 'side','price','re','unre', 'openposition','avgPrice']
    df= pd.DataFrame(index=index, columns=columns)
    df['sid']=1
    df['share']=randint(1,10)
    df['side']=df['side'].apply(lambda v: random.choice(['B','S']))
    df['price']=df['price'].apply(lambda v: randint(20,100))
    df['openposition']=0
    df['unre']=0
    df['avgPrice']=0
    for i in range (0,len(df.index)):
        if i==0:
            df.loc[:,'re']=0
            if df['side'][0]=='B':
                df['openposition'][0]=df['share'][0]
                df['avgPrice'][0]=float(df['price'][0])
            elif df['side'][0]=='S':
                df['openposition'][0]=-df['share'][0]
                df['avgPrice'][0]=float(df['price'][0])
        else:
            if df['side'][i]=='B':
                df['openposition'][i]=df['openposition'][i-1]+df['share'][i]
                if df['openposition'][i]>0:
                    df['avgPrice'][i]=(df['avgPrice'][i-1]*df['openposition'][i-1]+df['share'][i]*df['price'][i])/df['openposition'][i]
                elif df['openposition'][i]==0:
                    df['avgPrice'][i]=0
                else:
                    df['avgPrice'][i]=df['avgPrice'][i-1]
            if df['side'][i]=='S':
                df['openposition'][i]=df['openposition'][i-1]-df['share'][i]
                if df['openposition'][i]<0:
                    df['avgPrice'][i]=(abs(df['avgPrice'][i-1]*df['openposition'][i-1])+df['share'][i]*df['price'][i])/abs(df['openposition'][i])
                elif df['openposition'][i]==0:
                    df['avgPrice'][i]=0
                else:
                    df['avgPrice'][i]=df['avgPrice'][i-1]
            if abs(df['openposition'][i-1])-abs(df['openposition'][i])>0:
                if df['openposition'][i-1]>0:
                    df['re'][i]=(df['price'][i]-df['avgPrice'][i-1])*(df['share'][i])
                elif df['openposition'][i-1]<0:
                    df['re'][i]=(df['avgPrice'][i]-df['price'][i-1])*(df['share'][i])
            if abs(df['openposition'][i-1])-abs(df['openposition'][i])<0:
                if df['openposition'][i-1]>0:
                    df['unre'][i]=(df['price'][i]-df['avgPrice'][i-1])*(df['share'][i])
                elif df['openposition'][i-1]<0:
                    df['unre'][i]=(df['avgPrice'][i]-df['price'][i-1])*(df['share'][i])
    return df

class StrategPerformance(object):
    def __init__(self, df):
        self.df=df
        self.daily_return=df['re']
    def annualized_return(self):
        total_return=self.daily_return.sum()
        total_days = self.daily_return.index.size
        if total_return < -1:
            total_return = -1
        return ((1 + total_return)**(252 / total_days) - 1)

    def annualized_std(self):
        return np.sqrt(252) * np.std(self.daily_return)

    def annualized_downside_std(self):
        downside_return = self.daily_return.copy()
        downside_return[downside_return > 0] = 0
        return np.sqrt(252) * np.std(downside_return)

    def annual_vol(self):
        return self.annualized_std()

    def sharpe_ratio(self):
        stdev = self.annualized_std()
        if stdev == 0:
            return np.nan
        else:
            return self.annualized_return() / stdev

    def sortino_ratio(self):
        stdev = self.annualized_downside_std()
        if stdev == 0:
            return np.nan
        else:
            return self.annualized_return() / stdev

    def max_drawdown(self):
        return np.max(np.maximum.accumulate(self.daily_return) - self.daily_return)
        
df=dummy_dataframe()
print df
# sp=StrategPerformance(df)
# print sp.annualized_return(), sp.annualized_std(), sp.annualized_downside_std(), sp.annual_vol(), sp.sharpe_ratio()
