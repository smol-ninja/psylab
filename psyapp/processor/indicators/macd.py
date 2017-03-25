# -*- coding: utf-8 -*-
"""
Created on Thu Jul 07 02:05:12 2016

@author: Sagar
"""

def macd(macd_calc,sig =9,ema1= 12,ema2 = 26):
    macd_calc['EMA1'] = 0.0
    macd_calc['EMA1']= macd_calc['Open'].ewm(span = ema1,ignore_na=False, min_periods =0 ,adjust=True).mean()
    macd_calc['EMA2'] = 0.0
    macd_calc['EMA2']= macd_calc['Open'].ewm(span = ema2,ignore_na=False, min_periods =0 ,adjust=True).mean()
    macd_calc['macd'] = macd_calc['EMA1'] - macd_calc['EMA2']
    macd_calc['Signal_'+str(sig)] = 0.0
    macd_calc['Signal_'+str(sig)]= macd_calc['macd'].ewm(span = sig,ignore_na=False, min_periods =0 ,adjust=True).mean()
    del macd_calc['EMA1']
    del macd_calc['EMA2']
    return macd_calc