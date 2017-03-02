# -*- coding: utf-8 -*-
"""
Created on Thu Feb 02 03:59:19 2017

@author: sagar
"""

import datetime
from calendar import monthrange

def calc_days_left_nifty(date):
    """
    Input date: 'yyyy-mm-dd'
    return days left to next nifty Expiry
    """
    split_date = date.split('-')
    if len(split_date)!=3:
        print 'Check date'
        return -1
    month = int(split_date[1])
    year = int(split_date[0])
    day = int(split_date[2])
    a,max_days = monthrange(year, month)
    for i in range(1,max_days+1): 
        weekday = datetime.date(year,month,i).weekday()
        if weekday==3:
            last_thurs = i
    ndays = (datetime.date(year,month,last_thurs)- datetime.date(year,month,day)).days
    if ndays<1:
        if month<12:
            month+=1
            a,max_days = monthrange(year, month)
            for i in range(1,max_days+1): 
                weekday = datetime.date(year,month,i).weekday()
                if weekday==3:
                    last_thurs = i
            ndays = (datetime.date(year,month,last_thurs)- datetime.date(year,month-1,day)).days
        else:
            month=1
            year+=1
            a,max_days = monthrange(year, month)
            for i in range(1,max_days+1): 
                weekday = datetime.date(year,month,i).weekday()
                if weekday==3:
                    last_thurs = i
            ndays = (datetime.date(year,month,last_thurs)- datetime.date(year-1,12,day)).days            
    return ndays
