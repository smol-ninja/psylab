# -*- coding: utf-8 -*-
"""
Created on Thu Jul 07 02:57:53 2016

@author: Sagar
"""

def obv(obv_d):
    obv_d['obv'] =0
    for i in range(1,len(obv_d)): 
        if (obv_d.loc[i,'Close']-obv_d.loc[i-1,'Close']>0):
            obv_d.loc[i,'obv'] = obv_d.loc[i-1,'obv']+obv_d.loc[i,'Volume']
        else:
            obv_d.loc[i,'obv'] = obv_d.loc[i-1,'obv'] - obv_d.loc[i,'Volume']
    return obv_d