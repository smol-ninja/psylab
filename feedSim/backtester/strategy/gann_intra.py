# -*- coding: utf-8 -*-
"""
Created on Wed Feb 01 22:09:27 2017

@author: sagar
"""

import numpy as np
import pandas as pd
from orderObject import OrderObject

class StratDatabaseObject(object):
    def __init__(self,startPrice):
        self.startPrice = startPrice
        self.stopLoss = 7
        self.quantity = 20
        self.startQuantity = 20 
        self.quantity = 0
        self.buyPrice= startPrice
        self.sellPrice = startPrice
        self.targetReached = 0
        self.actionTarget = [.50,.25,.25]
        self.buyTarget = None
        self.sellTarget = None
        self.side =  'None'
        self.dayStart = True
        
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
    stratData = StratDatabaseObject(startPrice) 
    price = float(startPrice)
    gann = np.zeros(shape=(7,7))
    base_p = int(pow(price,0.5))
    gann = []
    drop_list = [10,12,14,16,18,20,22,24,26,27,29,30,32,33,35,36,38,39,41,42,44,45,47,48]
    for i in range(1,50):
        if i in drop_list:
            continue
        if i>25:
            gann.append(pow(base_p+1.0/24.0*(i-1),2))
        elif i>9:
            gann.append(pow(base_p+1.0/16.0*(i-9),2))
        elif i>1:
            gann.append(pow(base_p-1+1.0/8.0*(i-1),2))
        else:
            gann.append(pow(base_p-1,2))
    sup_levels = [i for i in gann if i > price]
    res_levels = [i for i in gann if i < price]
    res_levels.reverse()
    buy = sup_levels.pop(0)
    if int(pow(price,0.5))<> pow(price,0.5):
        sell = res_levels.pop(0)
    else:
        sell = price
    sup_levels = map(lambda x: x *1.0, sup_levels)
    res_levels = map(lambda x: x * 1.0, res_levels)
    stratData.buy = buy
    stratData.sell  = sell
    stratData.sellTarget  = res_levels
    stratData.buyTarget = sup_levels
    try:
        len(orderBook) # to check if orderBook exists or not
    except:
        orderBook = pd.DataFrame(columns = ['Date','Symbol','FuturePrice','Type','StrikePrice','Side','Quantity','Price','Value'])
    print startPrice
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

    if stratData.dayStart==False and stratData.quantity!=0: #day is about to end
        if stratData.side =='Buy':    
            orders.append(OrderObject(symbol = symbolObject.symbol,optionType = 'Fut',side = 'Sell',quantity = stratData.quantity))
        elif stratData.side=='Sell':
            orders.append(OrderObject(symbol = symbolObject.symbol,optionType = 'Fut',side = 'Buy',quantity = stratData.quantity))
        stratData.dayStart=True
    elif stratData.quantity!=0:
        if stckPrice<(stratData.buyPrice - stratData.stopLoss) and stratData.side=='Buy':
            orders.append(OrderObject(symbol = symbolObject.symbol,optionType = 'Fut',side = 'Sell',quantity = stratData.quantity))
            stratData.quantity=0
        elif stckPrice>(stratData.sellPrice + stratData.stopLoss) and stratData.side=='Sell':
            orders.append(OrderObject(symbol = symbolObject.symbol,optionType = 'Fut',side = 'Buy',quantity = stratData.quantity))
            stratData.quantity=0
        elif stratData.side=='Buy' and stratData.buyTarget[stratData.targetReached]<stckPrice:
            orders.append(OrderObject(symbol = symbolObject.symbol,optionType = 'Fut',side = 'Sell',quantity = stratData.startQuantity*stratData.actionTarget[stratData.targetReached]))
            stratData.quantity  -=stratData.startQuantity*stratData.actionTarget[stratData.targetReached]
            stratData.targetReached+=1
        elif stratData.side=='Sell' and stratData.sellTarget[stratData.targetReached]>stckPrice:
            orders.append(OrderObject(symbol = symbolObject.symbol,optionType = 'Fut',side = 'Buy',quantity = stratData.startQuantity*stratData.actionTarget[stratData.targetReached]))
            stratData.quantity  -=stratData.startQuantity*stratData.actionTarget[stratData.targetReached]
            stratData.targetReached+=1
    elif stratData.quantity==0 and stratData.side=='None':
        if stckPrice>stratData.buyPrice:
            orders.append(OrderObject(symbol = symbolObject.symbol,optionType = 'Fut',side = 'Buy',quantity = stratData.startQuantity))
            stratData.quantity= stratData.startQuantity
            stratData.side='Buy'
        elif stckPrice<stratData.sellPrice:
            orders.append(OrderObject(symbol = symbolObject.symbol,optionType = 'Fut',side = 'Sell',quantity = stratData.startQuantity))
            stratData.quantity= stratData.startQuantity
            stratData.side='Sell'
    return orders,stratData