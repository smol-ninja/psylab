# -*- coding: utf-8 -*-
"""
Created on Wed Feb 01 22:09:27 2017

@author: sagar
"""

import numpy as np
import pandas as pd
from create_trade_book import order_log
from orderObject import OrderObject
"""
Input:
    date
    startPrice
    sym
    strategy to be initialized here. First Orders and parameters set here
"""
def initialize_strategy(date,sym,startPrice):
    lastactionPrice = 235
    actionDif = 10
    openPrice= 235
    maxspell = 6
    stratData = [lastactionPrice,actionDif,openPrice,maxspell] 
    orders = []
    orders.append(OrderObject(symbol = sym,optionType = 'Put',strikePrice = int(lastactionPrice),side = 'Sell',quantity = 1))
    orders.append(OrderObject(symbol = sym,optionType = 'Call',strikePrice = int(lastactionPrice),side = 'Sell',quantity = 1))
    orderBook = pd.DataFrame(columns = ['Date','Symbol','FuturePrice','Type','StrikePrice','Side','Quantity','Price','Value'])
    orderBook = order_log(date,orders,orderBook,startPrice)
    return stratData,orderBook


"""
Input StckPrice , database,sym
return orderObject
    orderObject
    optiontype(str): Call,Put,Future
    strike(int): for future==0
    side(str): Buy, Sell
    quantity(int) 
"""
def strategy(stckPrice, stratData,sym):
    lastactionPrice = stratData[0]
    actionDif = stratData[1]
    openPrice = stratData[2]
    maxspell = stratData[3]
    orders = []
    if np.absolute(stckPrice-lastactionPrice)>actionDif and (stckPrice-lastactionPrice)*(stckPrice-openPrice)>0 and maxspell>abs(stckPrice-openPrice)/float(actionDif) and abs(openPrice-stckPrice)>actionDif:
        if lastactionPrice>stckPrice:
            orders.append(OrderObject(symbol = sym,optionType = 'Put',strikePrice = int(lastactionPrice-actionDif),side = 'Sell',quantity = 1))
            orders.append(OrderObject(symbol = sym,optionType = 'Call',strikePrice = int(lastactionPrice-actionDif),side = 'Sell',quantity = 1))
            lastactionPrice -= actionDif
        else:
            orders.append(OrderObject(symbol = sym,optionType = 'Put',strikePrice = int(lastactionPrice+actionDif),side = 'Sell',quantity = 1))
            orders.append(OrderObject(symbol = sym,optionType = 'Call',strikePrice = int(lastactionPrice+actionDif),side = 'Sell',quantity = 1))
            lastactionPrice += actionDif                   
    if np.absolute(stckPrice-lastactionPrice)>actionDif and ((stckPrice-lastactionPrice)*(stckPrice-openPrice)<0 or (abs(openPrice-stckPrice)<actionDif and (openPrice-lastactionPrice)*(openPrice-stckPrice)<0)):
        orders.append(OrderObject(symbol = sym,optionType = 'Put',strikePrice = int(lastactionPrice),side = 'Sell',quantity = 1))
        orders.append(OrderObject(symbol = sym,optionType = 'Call',strikePrice = int(lastactionPrice),side = 'Sell',quantity = 1))
        if lastactionPrice>stckPrice:
            lastactionPrice -= actionDif
        else:
            lastactionPrice += actionDif                      
    stratData = [lastactionPrice,actionDif,openPrice,maxspell]
    return orders,stratData