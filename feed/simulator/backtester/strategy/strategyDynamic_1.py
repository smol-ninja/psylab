# -*- coding: utf-8 -*-
"""
Created on Wed Feb 01 22:09:27 2017

@author: sagar
"""

import numpy as np
import pandas as pd
from create_trade_book import order_log
from orderObject import OrderObject

class StratDatabaseObject(object):
    def __init__(self):
        self.lastactionPrice = 250
        self.actionDif = 15
        self.openPrice = 250
        self.maxspell = 6
        self.quantity = 1

def initialize_strategy(date,symbolObject,startPrice):
    """
    Input:
        date
        startPrice
        symbolObject
        strategy to be initialized here. 
    return
        First Orders and parameters set here
    """
    stratData = StratDatabaseObject() 
    orders = []
    orders.append(OrderObject(symbol = symbolObject.symbol,optionType = 'Put',strikePrice = int(stratData.lastactionPrice),side = 'Sell',quantity = stratData.quantity))
    orders.append(OrderObject(symbol = symbolObject.symbol,optionType = 'Call',strikePrice = int(stratData.lastactionPrice),side = 'Sell',quantity = stratData.quantity))
    orderBook = pd.DataFrame(columns = ['Date','Symbol','FuturePrice','Type','StrikePrice','Side','Quantity','Price','Value'])
    orderBook = order_log(date,orders,orderBook,startPrice)
    return stratData,orderBook


def strategy(stckPrice, stratData,symbolObject):
    """
    Input StckPrice , database,sym
    return orderObject
        orderObject
        optiontype(str): Call,Put,Future
        strike(int): for future==0
        side(str): Buy, Sell
        quantity(int) 
    """
    lastactionPrice = stratData.lastactionPrice
    actionDif = stratData.actionDif
    openPrice = stratData.openPrice
    maxspell = stratData.maxspell
    orders = []
    if np.absolute(stckPrice-lastactionPrice)>actionDif and (stckPrice-lastactionPrice)*(stckPrice-openPrice)>0 and maxspell>abs(stckPrice-openPrice)/float(actionDif) and abs(openPrice-stckPrice)>actionDif:
        if lastactionPrice>stckPrice:
            orders.append(OrderObject(symbol = symbolObject.symbol,optionType = 'Put',strikePrice = int(lastactionPrice-actionDif),side = 'Sell',quantity = stratData.quantity))
            orders.append(OrderObject(symbol = symbolObject.symbol,optionType = 'Call',strikePrice = int(lastactionPrice-actionDif),side = 'Sell',quantity = stratData.quantity))
            lastactionPrice -= actionDif
        else:
            orders.append(OrderObject(symbol = symbolObject.symbol,optionType = 'Put',strikePrice = int(lastactionPrice+actionDif),side = 'Sell',quantity = stratData.quantity))
            orders.append(OrderObject(symbol = symbolObject.symbol,optionType = 'Call',strikePrice = int(lastactionPrice+actionDif),side = 'Sell',quantity = stratData.quantity))
            lastactionPrice += actionDif                   
    if np.absolute(stckPrice-lastactionPrice)>actionDif and ((stckPrice-lastactionPrice)*(stckPrice-openPrice)<0 or (abs(openPrice-stckPrice)<actionDif and (openPrice-lastactionPrice)*(openPrice-stckPrice)<0)):
        orders.append(OrderObject(symbol = symbolObject.symbol,optionType = 'Put',strikePrice = int(lastactionPrice),side = 'Buy',quantity = stratData.quantity))
        orders.append(OrderObject(symbol = symbolObject.symbol,optionType = 'Call',strikePrice = int(lastactionPrice),side = 'Buy',quantity = stratData.quantity))
        if lastactionPrice>stckPrice:
            lastactionPrice -= actionDif
        else:
            lastactionPrice += actionDif                      
    stratData.lastactionPrice = lastactionPrice
    return orders,stratData