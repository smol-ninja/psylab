import datetime
import pandas as pd
import random
from random import randint
import numpy as np

todays_date = datetime.datetime.now().date()

index = pd.date_range(todays_date-datetime.timedelta(10), periods=10, freq='D')

columns = ['sid','share', 'side','price','re','openvalue', 'openposition']
df= pd.DataFrame(index=index, columns=columns)
df['sid']=1
df['share']=randint(1,10)
df['side']=df['side'].apply(lambda v: random.choice(['B','S']))
df['price']=df['price'].apply(lambda v: randint(20,100))
df['openposition']=0
for i in range (0,len(df.index)):
    if i==0:
        df.loc[:,'re']=0
        if df['side'][0]=='B':
            df['openposition'][0]=df['share'][0]
            df['openvalue'][0]=df['share'][0]*df['price'][0]
        elif df['side'][0]=='S':
            df['openposition'][0]=-df['share'][0]
            df['openvalue'][0]=-df['share'][0]*df['price'][0]
    else:
        if df['side'][i]=='B':
            df['openposition'][i]=df['openposition'][i-1]+df['share'][i]
            df['openvalue'][i]=df['openvalue'][i-1]+df['share'][i]*df['price'][i]
            df['re'][i]=0
        elif df['side'][i]=='S':
            df['openposition'][i]=df['openposition'][i-1]-df['share'][i]
            df['openvalue'][i]=df['openvalue'][i-1]-df['share'][i]*df['price'][i]
            df['re'][i]=df['share'][i]*(df['price'][i-1]-df['price'][i])

print df

def performance(df):
    stats={}
    daily_return=df['re']
    print daily_return
    stats['Annual Return'] = annualized_return(daily_return)
    stats['Annual Vol'] = annual_vol(daily_return)
    stats['Sharpe Ratio'] = sharpe_ratio(daily_return)
    stats['Sortino Ratio'] = sortino_ratio(daily_return)
    stats['Max Drawdown'] = max_drawdown(daily_return)
    return stats

def annualized_return(daily_return):
    total_return = daily_return.sum()
    total_days = daily_return.index.size
    if total_return < -1:
        total_return = -1
    return ((1 + total_return)**(252 / total_days) - 1)

def annualized_std(daily_return):
    return np.sqrt(252) * np.std(daily_return)

def annualized_downside_std(daily_return):
    downside_return = daily_return.copy()
    downside_return[downside_return > 0] = 0
    return np.sqrt(252) * np.std(downside_return)

def annual_vol(daily_return):
    return annualized_std(daily_return)

def sharpe_ratio(daily_return):
    stdev = annualized_std(daily_return)
    if stdev == 0:
        return np.nan
    else:
        return annualized_return(daily_return) / stdev
def sortino_ratio(daily_return):

    stdev = annualized_downside_std(daily_return)
    if stdev == 0:
        return np.nan
    else:
        return annualized_return(daily_return) / stdev

def max_drawdown(daily_return):
    return np.max(np.maximum.accumulate(daily_return) - daily_return)

print performance(df)
