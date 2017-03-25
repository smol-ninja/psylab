# -*- coding: utf-8 -*-
"""
Created on Thu Jul 07 02:57:53 2016

@author: Sagar
"""
def mfi(mfi_d,win=9):
    mfi_d['typicalPrice'] = (mfi_d['High']+mfi_d['Low']+mfi_d['Close'])/3.0
    mfi_d['flowMoney'] = mfi_d['typicalPrice']*mfi_d['Volume']
    mfi_d['1pflow'] =0 
    mfi_d['1mflow'] =0
    mfi_d['14pflow'] =0
    mfi_d['14mflow'] = 0
    for i in range(1,len(mfi_d)): 
        if (mfi_d.loc[i,'typicalPrice']-mfi_d.loc[i-1,'typicalPrice']>0):
            mfi_d.loc[i,'1pflow'] = mfi_d.loc[i,'flowMoney']
        else:
            mfi_d.loc[i,'1mflow'] = mfi_d.loc[i,'flowMoney']
        if i==win:
            mfi_d.loc[i,'14pflow'] = mfi_d['1pflow'][1+i-win:1+win].mean()
            mfi_d.loc[i,'14mflow'] = mfi_d['1mflow'][1+i-win:1+win].mean()
        elif i>win:            
            mfi_d.loc[i,'14pflow'] = mfi_d['1pflow'][i-win+1:i+1].mean()
            mfi_d.loc[i,'14mflow'] = mfi_d['1mflow'][1+i-win:1+i].mean()
    mfi_d['mfRatio'] = mfi_d['14pflow']/mfi_d['14mflow']
    mfi_d['mfi'] = 100.0 - 100.0/(mfi_d['mfRatio']+1)
    return mfi_d