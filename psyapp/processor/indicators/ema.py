# -*- coding: utf-8 -*-
"""
Created on Thu Jul 07 02:05:12 2016

@author: Sagar
"""

def ema(ema_calc,pd = 200):
    ema_calc['ema_'+str(pd)] = 0.0
    ema_calc['ema_'+str(pd)]= ema_calc['Close'].ewm(span = pd,ignore_na=False, min_periods =0 ,adjust=True).mean()
    return ema_calc