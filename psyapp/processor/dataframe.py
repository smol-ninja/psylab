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
                sid  share side  price  re  unre  openposition  avgPrice
    2017-05-07    1      2    B     23   0   0.0             2      23.0
    2017-05-08    1      2    S     30  14   0.0             0       0.0
    2017-05-09    1      2    B     29  14   0.0             2      29.0
    2017-05-10    1      2    B     66  14  74.0             4      47.5
    2017-05-11    1      2    S     27 -27   0.0             2      47.5
    2017-05-12    1      2    S     54 -14   0.0             0       0.0
    2017-05-13    1      2    B     48 -14   0.0             2      48.0
    2017-05-14    1      2    S     30 -50   0.0             0       0.0
    2017-05-15    1      2    S     63 -50   0.0            -2      63.0
    2017-05-16    1      2    S     56 -50  14.0            -4      59.5
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
    df['unre']=0.0
    df['avgPrice']=0.0
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
            # import pdb; pdb.set_trace()
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
                    df['re'][i]=((df['price'][i]-df['avgPrice'][i-1])*(df['share'][i]))+df['re'][i-1]
                elif df['openposition'][i-1]<0:
                    df['re'][i]=((df['avgPrice'][i-1]-df['price'][i])*(df['share'][i]))+df['re'][i-1]
                else:
                    df['re'][i]=df['re'][i-1]
            if abs(df['openposition'][i-1])-abs(df['openposition'][i])<0:
                if df['openposition'][i-1]>0:
                    df['unre'][i]=(df['price'][i]-df['avgPrice'][i-1])*(df['share'][i])
                    df['re'][i]=df['re'][i-1]
                elif df['openposition'][i-1]<0:
                    df['unre'][i]=(df['avgPrice'][i-1]-df['price'][i])*(df['share'][i])
                    df['re'][i]=df['re'][i-1]
                else:
                    df['re'][i]=df['re'][i-1]
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

    def volatility(self):
        self.stock_change=[]
        self.index_change=[]
        # TODO: use fetch Data function to fetch price of refrence Index
        for i in range (0,len(self.df.index)):
            try:
                self.stock_change.append(((df['price'][i+1]-df['price'][i])/df['price'][i])*100)
            except Exception as e:
                pass
        return numpy.cov(self.stock_change, self.index_change)[0][1]

    def winloss_rate(self):
        win=0
        loss=0
        last_index=len(self.df.index)
        for i in range (0,last_index):
            try:
                if df['re'][i+1]-df['re'][i] > 0:
                    win+=1
                elif df['re'][i+1]-df['re'][i] < 0:
                    loss+=1
            except Exception as e:
                pass
        if df['openposition'][last_index-1] < 0:
            if df['avgPrice'][last_index-1] > df['price'][last_index-1]:
                win+=(abs(df['openposition'][last_index-1])/df['share'][0])
            elif df['avgPrice'][last_index-1] < df['price'][last_index-1]:
                loss+=(abs(df['openposition'][last_index-1])/df['share'][0])
        elif df['openposition'][last_index-1] > 0:
            if df['avgPrice'][last_index-1]<= df['price'][last_index-1]:
                win+=(abs(df['openposition'][last_index-1])/df['share'][0])
            elif df['avgPrice'][last_index-1] > df['price'][last_index-1]:
                loss+=(abs(df['openposition'][last_index-1])/df['share'][0])
        return {'win':round(win/(win+loss),2), 'loss':round(loss/(win+loss),2)}

df=dummy_dataframe()
print df
sp=StrategPerformance(df)
print sp.annualized_return(), sp.annualized_std(), sp.annualized_downside_std(), sp.annual_vol(), sp.sharpe_ratio(), sp.winloss_rate()
