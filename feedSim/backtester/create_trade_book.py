# -*- coding: utf-8 -*-
"""
Created on Thu Feb 02 03:33:37 2017

@author: sagar
"""
from optionPricePredictor import calc_premium
from estimate_expiry import calc_days_left_nifty
import datetime

def order_log(dateObject,orders,orderBook,futurePrice):
    """
    Input:
        date
        orderObject
            optiontype(str): Call,Put,Future
            strikePrice(int): for future==0
            side(str): Buy, Sell
            quantity(int) 
        orderBook(DataFrame)
        futurePrice(float): stockPrice
    returns OrderBook(DataFrame)
    """    
    nordersPast = len(orderBook)
    for i in range(len(orders)):
        order = orders[i]
        sym = order.symbol
        optionType = order.optionType
        if optionType!='Fut':
            strikePrice = int(order.strikePrice)
        else:
            strikePrice = 0
        side = order.side
        quantity = int(order.quantity)
        orderPrice= 0
        date = dateObject.strftime('%Y-%m-%d')
        if (optionType=='Call' or optionType=='Put') and strikePrice>0:
            daysLeft = calc_days_left_nifty(date)
            timeLeft = datetime.datetime.combine(datetime.date.today(), datetime.time(15,30,00)) - datetime.datetime.combine(datetime.date.today(), dateObject.time())
            totalTimeLeft = daysLeft + timeLeft.seconds/22501.0
            orderPrice = calc_premium(int(futurePrice),optionType,strikePrice,totalTimeLeft)
        elif optionType=='Fut':
            orderPrice = futurePrice
            strikePrice = 0
        if side=='Buy':
            orderValue = -orderPrice*quantity
        elif side=='Sell':            
            orderValue = orderPrice*quantity
        orderBook.loc[nordersPast+i] = [date,sym,futurePrice,optionType,strikePrice,side,quantity,orderPrice,orderValue]
    return orderBook


def PnL_log(orderBook,expiryPrice):
    """
    Input:
        orderBook
        expiryPrice
    return PnL report
    """
    orderBook.loc[:,'ExpiryPrice'] = expiryPrice
    orderBook.loc[:,'PnL'] = 0
    for i in range(len(orderBook)):
        if orderBook.loc[i,'Type']!='Fut':
            if orderBook.loc[i,'Type']=='Call':
                callPrice= expiryPrice - orderBook.loc[i,'StrikePrice'] 
                if callPrice<0:
                    callPrice = 0 
                orderBook.loc[i,'ExpiryPrice'] = callPrice
            elif orderBook.loc[i,'Type']=='Put':
                putPrice= -expiryPrice + orderBook.loc[i,'StrikePrice'] 
                if putPrice<0:
                    putPrice = 0 
                orderBook.loc[i,'ExpiryPrice'] = putPrice
        if orderBook.loc[i,'Side']=='Buy':
            finalValue = orderBook.loc[i,'ExpiryPrice']*orderBook.loc[i,'Quantity']
        elif orderBook.loc[i,'Side']=='Sell':
            finalValue = -orderBook.loc[i,'ExpiryPrice']*orderBook.loc[i,'Quantity']
        orderBook.loc[i,'PnL'] = finalValue + orderBook.loc[i,'Value']
    return orderBook