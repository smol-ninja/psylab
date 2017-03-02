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
        self.actionDif = 100
        self.quantity = 1
        self.callR = 3
        self.putR = 3
        self.actionrange= [startPrice-self.putR*self.actionDif,startPrice+self.callR*self.actionDif]

        
def initialize_strategy(dateObejct,symbolObject,startPrice,orderBook=None):
    """
    Input:
        dateObject
        startPrice
        symbolObject
        strategy to be initialized here. 
    return
        First Orders and parameters set here
    """
    stratData = StratDatabaseObject(round(startPrice,-2)) 
    orders = []

    orderBook = pd.DataFrame(columns = ['Date','Symbol','FuturePrice','Type','StrikePrice','Side','Quantity','Price','Value'])
    orders.append(OrderObject(symbol = symbolObject.symbol,optionType = 'Put',strikePrice = stratData.actionrange[0],side = 'Sell',quantity = stratData.quantity))
    orders.append(OrderObject(symbol = symbolObject.symbol,optionType = 'Call',strikePrice = stratData.actionrange[1],side = 'Sell',quantity = stratData.quantity))
    orderBook = order_log(dateObejct,orders,orderBook,startPrice)
   
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
    prevActionRange = stratData.actionrange[:]
    if stckPrice-(stratData.putR-1)*stratData.actionDif<=stratData.actionrange[0]:
        if stratData.putR>=3:
            stratData.putR=2
            stratData.actionrange[1] = stratData.actionrange[0]+(stratData.callR+stratData.putR)*stratData.actionDif
        elif stratData.putR==2:
            stratData.actionrange[0] = stratData.actionrange[0] - stratData.actionDif 
            stratData.actionrange[1] = stratData.actionrange[1] - stratData.actionDif 
    if stckPrice+(stratData.callR-1)*stratData.actionDif>=stratData.actionrange[1]:
        if stratData.callR>=3:
            stratData.callR=2
            stratData.actionrange[0] = stratData.actionrange[1]-(stratData.callR+stratData.putR)*stratData.actionDif
        elif stratData.callR==2:
            stratData.actionrange[0] = stratData.actionrange[0] + stratData.actionDif 
            stratData.actionrange[1] = stratData.actionrange[1] + stratData.actionDif 
    if stratData.actionrange[0]!=prevActionRange[0]:
        orders.append(OrderObject(symbol = symbolObject.symbol,optionType = 'Put',strikePrice = prevActionRange[0],side = 'Buy',quantity = stratData.quantity))
        orders.append(OrderObject(symbol = symbolObject.symbol,optionType = 'Put',strikePrice = stratData.actionrange[0],side = 'Sell',quantity = stratData.quantity))
    if stratData.actionrange[1]!=prevActionRange[1]:
        orders.append(OrderObject(symbol = symbolObject.symbol,optionType = 'Call',strikePrice = prevActionRange[1],side = 'Buy',quantity = stratData.quantity))
        orders.append(OrderObject(symbol = symbolObject.symbol,optionType = 'Call',strikePrice = stratData.actionrange[1],side = 'Sell',quantity = stratData.quantity))
        
            
    return orders,stratData