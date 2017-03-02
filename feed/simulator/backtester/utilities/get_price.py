# -*- coding: utf-8 -*-
"""
Created on Fri Feb 03 13:29:27 2017

@author: sagar
"""

def get_priceByDate(sym,masterData,date):
    """
    Input:
        sym
        masterdata(DataFrame): contains (O,H,L,C) data
        date: data of date required yyyy-mm-dd
    returns (O,H,L,C)
    """
    dayData = masterData.loc[masterData['Date'] == date]
    openP = int(dayData['Open'])
    closeP = int(dayData['Close'])
    highP = int(dayData['High'])
    lowP = int(dayData['Low'])
    return openP,highP,lowP,closeP

def get_price_startEnd(masterData,time):
    """
    Input:
        masterData
        time(Str): start,end
    return openPrice of masterData or closePrice of masterData
    """
    if time =='End':
        return masterData.loc[len(masterData)-1]['Close']
    elif time == 'Start':
        return masterData.loc[0]['Open']
    else:
        print 'Select Start or End'
        return -1