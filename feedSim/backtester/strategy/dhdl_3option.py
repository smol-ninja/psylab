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
        self.curPos = "None"
        self.prevLow = startPrice
        self.prevHigh = startPrice
        self.quantity = 1
        self.prevATMpos = startPrice

        
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
    atmPrice = round(stckPrice,-2)
    if stratData.curPos=="Buy" and stckPrice<stratData.prevLow:        
        orders.append(OrderObject(symbol = symbolObject.symbol, optionType = 'Call', strikePrice = atmPrice, side = 'Sell', quantity = stratData.quantity))
        orders.append(OrderObject(symbol = symbolObject.symbol, optionType = 'Call', strikePrice = atmPrice-100, side = 'Sell', quantity = stratData.quantity))
        orders.append(OrderObject(symbol = symbolObject.symbol, optionType = 'Call', strikePrice = atmPrice+100, side = 'Sell', quantity = stratData.quantity))
        orders.append(OrderObject(symbol = symbolObject.symbol, optionType = 'Put', strikePrice = stratData.prevATMpos, side = 'Buy', quantity = stratData.quantity))
        orders.append(OrderObject(symbol = symbolObject.symbol, optionType = 'Put', strikePrice = stratData.prevATMpos-100, side = 'Buy', quantity = stratData.quantity))
        orders.append(OrderObject(symbol = symbolObject.symbol, optionType = 'Put', strikePrice = stratData.prevATMpos+100, side = 'Buy', quantity = stratData.quantity))
        stratData.prevATMpos = atmPrice
        stratData.curPos="Sell"
    elif stratData.curPos=="Sell" and stckPrice>stratData.prevHigh:
        orders.append(OrderObject(symbol = symbolObject.symbol, optionType = 'Put', strikePrice = atmPrice, side = 'Sell', quantity = stratData.quantity))
        orders.append(OrderObject(symbol = symbolObject.symbol, optionType = 'Put', strikePrice = atmPrice-100, side = 'Sell', quantity = stratData.quantity))
        orders.append(OrderObject(symbol = symbolObject.symbol, optionType = 'Put', strikePrice = atmPrice+100, side = 'Sell', quantity = stratData.quantity))
        orders.append(OrderObject(symbol = symbolObject.symbol, optionType = 'Call', strikePrice = stratData.prevATMpos, side = 'Buy', quantity = stratData.quantity))
        orders.append(OrderObject(symbol = symbolObject.symbol, optionType = 'Call', strikePrice = stratData.prevATMpos-100, side = 'Buy', quantity = stratData.quantity))
        orders.append(OrderObject(symbol = symbolObject.symbol, optionType = 'Call', strikePrice = stratData.prevATMpos+100, side = 'Buy', quantity = stratData.quantity))
        stratData.prevATMpos = atmPrice
        stratData.curPos="Buy"
    elif stratData.curPos=="None" and stratData.prevHigh != stratData.prevLow:
        if stckPrice>stratData.prevHigh:
            orders.append(OrderObject(symbol = symbolObject.symbol, optionType = 'Put', strikePrice = atmPrice, side = 'Sell', quantity = stratData.quantity))
            orders.append(OrderObject(symbol = symbolObject.symbol, optionType = 'Put', strikePrice = atmPrice-100, side = 'Sell', quantity = stratData.quantity))
            orders.append(OrderObject(symbol = symbolObject.symbol, optionType = 'Put', strikePrice = atmPrice+100, side = 'Sell', quantity = stratData.quantity))
            stratData.prevATMpos = atmPrice
            stratData.curPos="Buy"
        elif  stckPrice<stratData.prevLow:             
            orders.append(OrderObject(symbol = symbolObject.symbol, optionType = 'Call', strikePrice = atmPrice, side = 'Sell', quantity = stratData.quantity))
            orders.append(OrderObject(symbol = symbolObject.symbol, optionType = 'Call', strikePrice = atmPrice-100, side = 'Sell', quantity = stratData.quantity))
            orders.append(OrderObject(symbol = symbolObject.symbol, optionType = 'Call', strikePrice = atmPrice+100, side = 'Sell', quantity = stratData.quantity))
            stratData.prevATMpos = atmPrice
            stratData.curPos="Sell"

    return orders,stratData