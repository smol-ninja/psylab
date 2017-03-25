# -*- coding: utf-8 -*-
"""
Created on Thu Mar 09 20:30:41 2017

@author: sagar
"""

def dayHighLow(dhdl,previousDays = 1):    
    dhdl['PrevHigh_'+str(previousDays)] = 0
    dhdl['PrevLow_'+str(previousDays)] = 0
    for i in range(len(dhdl)):
        if i<previousDays:
            continue
        else:
            dhdl.loc[i, 'PrevHigh_'+str(previousDays)] = dhdl.loc[i-previousDays,'High']
            dhdl.loc[i, 'PrevLow_'+str(previousDays)] = dhdl.loc[i-previousDays,'Low']
    return dhdl