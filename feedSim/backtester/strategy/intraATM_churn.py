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
    def __init__(self,startPrice):
        self.startPrice = startPrice
        self.lastActionPrice = startPrice
        self.churningValue = 10
        self.churnQuantity = 1
        self.quantity = 10
        self.startQunatity = 10
        self.dayStart = True
        self.maxExposure= 10
        
def initialize_strategy(dateObject,symbolObject,startPrice,orderBook=None):
    """
    Input:
        date
        startPrice
        symbolObject
        strategy to be initialized here. 
    return
        First Orders and parameters set here
    """
    stratData = StratDatabaseObject(round(startPrice,-2)) 
    orders = []

    try:
        len(orderBook) # to check if orderBook exists or not
    except:
        orderBook = pd.DataFrame(columns = ['Date','Symbol','FuturePrice','Type','StrikePrice','Side','Quantity','Price','Value'])

    orders.append(OrderObject(symbol = symbolObject.symbol,optionType = 'Put',strikePrice = stratData.startPrice,side = 'Sell',quantity = stratData.startQunatity))
    orders.append(OrderObject(symbol = symbolObject.symbol,optionType = 'Call',strikePrice = stratData.startPrice,side = 'Sell',quantity = stratData.startQunatity))
    orderBook = order_log(dateObject,orders,orderBook,startPrice)
    stratData.quantity = stratData.startQunatity
    
    return stratData, orderBook


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
    orders = []

    if stratData.dayStart==False: #day is about to end
        orders.append(OrderObject(symbol = symbolObject.symbol,optionType = 'Put',strikePrice = int(stratData.startPrice),side = 'Buy',quantity = stratData.quantity))
        orders.append(OrderObject(symbol = symbolObject.symbol,optionType = 'Call',strikePrice = int(stratData.startPrice),side = 'Buy',quantity = stratData.quantity))
        stratData.dayStart=True
    else:
        if stratData.quantity<stratData.maxExposure and abs(stratData.lastActionPrice - stckPrice)>stratData.churningValue:
            if (stratData.startPrice - stckPrice)*(stratData.lastActionPrice - stckPrice)>0:
                orders.append(OrderObject(symbol = symbolObject.symbol,optionType = 'Put',strikePrice = stratData.startPrice,side = 'Sell',quantity = stratData.churnQuantity))
                orders.append(OrderObject(symbol = symbolObject.symbol,optionType = 'Call',strikePrice = stratData.startPrice,side = 'Sell',quantity = stratData.churnQuantity))
                stratData.quantity +=  stratData.churnQuantity
            else:
                orders.append(OrderObject(symbol = symbolObject.symbol,optionType = 'Put',strikePrice = stratData.startPrice,side = 'Buy',quantity = stratData.churnQuantity))
                orders.append(OrderObject(symbol = symbolObject.symbol,optionType = 'Call',strikePrice = stratData.startPrice,side = 'Buy',quantity = stratData.churnQuantity))
                stratData.quantity -=  stratData.churnQuantity
            stratData.lastActionPrice = stckPrice
                
    return orders,stratData