# -*- coding: utf-8 -*-
"""
Created on Thu Jul 07 01:33:57 2016

@author: Sagar
"""
import pandas as pd
import urllib2
def read_data(stock,start_date,end_date,freq='d'):
    """
    Imput: 
    symbol -  (str)
    startDate,endDate(str) - yyyy-mm-dd  
    return:
        pandas dataset
    """
    start_date_list = start_date.split('-')
    end_date_list = end_date.split('-')
    if stock =='NIFTY':
        stock = '%5ENSEI'
    else:
        stock +='.BO'
    if len(start_date_list)!=3 or len(start_date_list)!=3:
        print 'Incorrect format'
        return -1
    else:
        for i in range(len(start_date_list)):
            start_date_list[i]  = int(start_date_list[i])
            end_date_list[i]  = int(end_date_list[i])
        if start_date_list[2]>31 or end_date_list[2]>31 or start_date_list[1]>12 or end_date_list[1]>12:
            print 'Check Date'
            return -1
    start_d = start_date_list[2]
    start_m = start_date_list[1]-1
    start_y = start_date_list[0]
    end_d = end_date_list[2]
    end_m = end_date_list[1]-1
    end_y = end_date_list[0]
    link = 'http://real-chart.finance.yahoo.com/table.csv?s='+stock+'&d='+str(end_m)+'&e='+str(end_d)+'&f='+str(end_y)+'&g='+freq+'&a='+str(start_m)+'&b='+str(start_d)+'&c='+str(start_y)+'&ignore=.csv'
    try:
        data = pd.read_csv(link)
    except urllib2.HTTPError:
        print 'Symbol Not Found'
        return -1
    data.sort_index(axis=0,ascending=False,inplace=True)
    data.index = range(len(data))
    return data
