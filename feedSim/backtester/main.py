# -*- coding: utf-8 -*-
"""
Created on Thu Feb 02 02:37:33 2017

@author: sagar
"""

#from results_params import calc_strategy_params
from strategy.gann_intra import strategy, initialize_strategy
from fetch_master_data import read_data
from create_trade_book import order_log, PnL_log
from utilities.get_price import get_priceByDate, get_price_startEnd
from utilities.priceSimulator import SymbolObject, PriceSimulator
import os
import datetime

# Initilize parameters

sym = SymbolObject(symbol='NIFTY', optionType='Future', strikePrice=8600)
tradeStart = '2016-09-01'
tradeEnd = '2017-01-25'
masterData = read_data(sym.symbol, tradeStart, tradeEnd)

#Initialize strategy
startPrice = get_price_startEnd(masterData, 'Start')

#Simulation Begins
path = "simulatedData.txt"

try:
    os.remove(path)
except:
    pass
priceList= []

with open(path, "a+") as f:
    for i in range(len(masterData)):
        date = masterData.loc[i,'Date']       
        daystockPrices = get_priceByDate(sym,masterData,date)
        test = PriceSimulator(sym, startPriceFuture = daystockPrices[0])
        test.initializeDataPoints(ndays = 1, OHLCList = list(daystockPrices), probabilityOfSpikeIntraday =3e-8, probabilityOfSpikeDayOpen = 1e-8)
        try:
            strategyDataBase,orderBook = initialize_strategy( datetime.datetime.strptime(date ,'%Y-%m-%d').replace(hour=9,minute=15),symbolObject = sym, startPrice= daystockPrices[0], orderBook = orderBook)
        except:
            strategyDataBase,orderBook = initialize_strategy( datetime.datetime.strptime(date ,'%Y-%m-%d').replace(hour=9,minute=15), symbolObject = sym, startPrice= daystockPrices[0])
            
        for key in test.simulatedPrices.keys():
            for priceObject in test.simulatedPrices[key]:
                dateTimeObject = datetime.datetime.strptime(str(date) + " " + str(priceObject.timeStamp.time()),'%Y-%m-%d %H:%M:%S')                
                test.runSimulator(priceObject)
                stockPrice = priceObject.futPrice
                order, strategyDataBase = strategy(stockPrice, strategyDataBase, sym)
                stringToPrint = str(priceObject.timeStamp.date()) + ', ' + str(priceObject.timeStamp.time()) + ', ' + str(priceObject.futPrice) + ', ' + str(priceObject.optionPrice)+ '\n'
                f.write(stringToPrint)
                priceList.append(stockPrice)
                if len(order)>0:
                    orderBook = order_log(dateTimeObject, order, orderBook, stockPrice)
        strategyDataBase.dayStart=False
        order, strategyDataBase = strategy(stockPrice, strategyDataBase, sym)
        orderBook = order_log(dateTimeObject, order, orderBook, stockPrice)
#        prevHigh = masterData.loc[i,'High']
#        prevLow = masterData.loc[i,'Low']
#        strategyDataBase.prevHigh = prevHigh
#        strategyDataBase.prevLow = prevLow

expiryPrice = get_price_startEnd(masterData,'End')
final_trade_book = PnL_log(orderBook,expiryPrice)
sum(final_trade_book['PnL'])

####### Testing #########

#profits_list = [1, 2, 4, 14, 13, 1, 2, -2, -12, 214, 12, -12]
#calc_strategy_params(profits_list, 40, 'monthly')

import matplotlib.pyplot as plt
#%matplotlib qt
plt.figure(1)
plt.plot(priceList)