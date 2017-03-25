# -*- coding: utf-8 -*-
"""
Created on Thu Mar 09 20:41:56 2017

@author: abc
"""


def roc(roc_data, col_name, pd = 10):
    if pd<=0:
        print 'Period of ROC must be greate than 0'
        raise IOError
    else: 
        roc_data['roc_'+ col_name] = 0 
        for i in range(len(roc_data)):
            if i<pd:
                continue
            else:
                roc_data.loc[i, 'roc_'+ col_name] = (roc_data.loc[i, col_name] - roc_data.loc[i-pd, col_name])/float(pd)
    return roc_data