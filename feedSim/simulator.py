# -*- coding: utf-8 -*-
"""
Created on Fri Feb 03 13:52:05 2017

@author: Sagar
"""

import urllib2
import random
import datetime
import numpy as np
from optionPricePredictor import calc_premium
import warnings

class PriceByTimeObject(object):
    def __init__(self, timeStamp, symbolObject, futPrice=0, optionPrice = 0):
        self.timeStamp = timeStamp
        self.futPrice = futPrice
        self.symbol = symbolObject
        self.optionPrice = optionPrice

class SymbolObject(object):
    def __init__(self, symbol, optionType = 'Future', strikePrice = 0):
        self.symbol = symbol
        if optionType not in ['Future','Call','Put']:
            print 'Incorrect optionType'
            raise IOError
        elif optionType!='Future' and strikePrice<0:
            print 'Incorrect StrikePrice'
            raise IOError
        elif optionType=='Call' or optionType=='Put':
            self.strikePrice = strikePrice
        if optionType=='Future':
            self.strikePrice = 0
        self.optionType = optionType

class Simulator(object):
    """
    Feed Simulator.
    Returns a Dictionary with keys as day and value as list of PriceByTimeObject
    """
    def __init__(self, SymbolObject, startPriceFuture=-1):
        self.symbolObj = SymbolObject
        self.__optionType = SymbolObject.optionType
        if startPriceFuture>0:
            self.startPrice = startPriceFuture
        elif startPriceFuture!=-1:
            print 'Start Price cant be less than equal to zero.'
            raise IOError
        elif startPriceFuture==-1:
            try:
                self.startPrice = float(urllib2.urlopen('http://finance.google.com/finance/info?client=ig&q=NSE:'+self.symbolObj.symbol).read().split(':')[5].split('"')[1])
            except urllib2.HTTPError:
                print 'Symbol Not Found. Default start Price = 100'
                self.startPrice = 100


    def initializeDataPoints(self, OHLCList=None, priceMovementList=None, ndays = 1, probabilityOfSpikeIntraday = 1e-8, probabilityOfSpikeDayOpen = 5e-3,startDaysLeft = None):
        """
        Initializes simulated Prices objects and fixed data points for prices to move to.
        OHLC (list): Open, High, Low, Close of the time frame to be simulated
        priceMovementList (list): fixed points for prices to move from
        ndays (int): number of days to simulate
        """
        warnings.simplefilter('ignore', np.RankWarning)
        self.ndays = int(ndays)
        if startDaysLeft<0:
            self.startDaysLeft = self.ndays
        else:
            self.startDaysLeft = startDaysLeft
        self.simulatedPrices = {}
        startTimeNSE = datetime.datetime(100, 1, 1, 9, 15, 00)
        for day in range(self.ndays):
            for timestep in range(22500):
                priceObject = PriceByTimeObject(timeStamp = startTimeNSE+datetime.timedelta(day, timestep), symbolObject = self.symbolObj)
                try:
                    self.simulatedPrices[day].append(priceObject)
                except KeyError:
                    self.simulatedPrices[day] = [priceObject]

        if OHLCList!=None and len(OHLCList)!=4:
            print 'Input (O,H,L,C) list format is incorrect'
            raise IOError
        elif OHLCList!=None and priceMovementList!=None:
            print 'Input either (O,H,L,C) or price path movement'
            raise IOError
        elif OHLCList!=None and type(OHLCList)==list:
            if (OHLCList[1]-OHLCList[0])*(OHLCList[3]-OHLCList[2])<(OHLCList[1]-OHLCList[3])*(OHLCList[0]-OHLCList[2]):
                flag_HighBeforeLow=1
            else:
                flag_HighBeforeLow=0
            if flag_HighBeforeLow==1:
                self.priceMovementList = [OHLCList[0], OHLCList[1], OHLCList[2], OHLCList[3]]
            else:
                self.priceMovementList = [OHLCList[0], OHLCList[2], OHLCList[1], OHLCList[3]]
        elif priceMovementList!=None and type(priceMovementList)==list:
            self.priceMovementList = priceMovementList
        else:
            averagePriceMovementPerDay = 50
            randomNumber_priceUpDown = random.randrange(-1, 2, 2)
            self.priceMovementList = [self.startPrice, self.startPrice + randomNumber_priceUpDown*round(random.random(),2)*self.ndays*averagePriceMovementPerDay]

        self.HighPrice = max(self.priceMovementList)
        self.LowPrice = min(self.priceMovementList)

        if probabilityOfSpikeIntraday>1 or probabilityOfSpikeIntraday<0:
            print 'Incorrect Probability '
            raise IOError
        else:
            self.probabilityOfSpikeIntraday = probabilityOfSpikeIntraday
        if probabilityOfSpikeDayOpen>1 or probabilityOfSpikeDayOpen<0:
            print 'Incorrect Probability '
            raise IOError
        else:
            self.probabilityOfSpikeDayOpen = probabilityOfSpikeDayOpen


        self.__priceMovementLeft = self.priceMovementList
        self.__lastPricepriceObject = self.simulatedPrices[0][0]
        self.__xIndex=0
        if len(self.__priceMovementLeft)==2:
            self.__xCordinatesPrice = [0, self.ndays*22500-1]
        elif len(self.__priceMovementLeft)>2:
            self.__xCordinatesPrice = [0]
            for i in range(len(self.__priceMovementLeft)-2):
                randomNumber_xCordinate = random.random()
                xCordinatewrtPrevious = int((i + randomNumber_xCordinate)*(22500*self.ndays/(len(self.__priceMovementLeft)-2)))
                self.__xCordinatesPrice.append(xCordinatewrtPrevious)
            self.__xCordinatesPrice.append(self.ndays*22500-1)
        self.__xCordinatesPriceLeft  = self.__xCordinatesPrice[:]


    def __simulateIntradayPriceSpikes(self, priceObject):
        """
        Simulates intraday Price Spikes with a probability
        """
        randomNumber_spike = random.randint(1,int(1/self.probabilityOfSpikeIntraday))
        randomNumber_priceUpDown = random.randrange(-1, 2, 2)
        randomNumber_percentageChange = random.random()/2.0
        if randomNumber_spike==1:
            priceObject.futPrice= priceObject.futPrice*(1+randomNumber_priceUpDown*randomNumber_percentageChange/100.0)


    def __simulateDayOpenPrice(self, priceObject):
        """
        Simulates day open price with a probability of a spike
        """
        if priceObject.timeStamp == datetime.datetime(100, 1, 1, 9, 15):
            randomNumber_spike = random.randint(1,int(1/self.probabilityOfSpikeDayOpen))
            randomNumber_priceUpDown = random.randrange(-1, 2, 2)
            if randomNumber_spike==1:
                randomNumber_percentageChange = random.random()*2.0
                priceObject.futPrice= priceObject.futPrice*(1+(randomNumber_priceUpDown*randomNumber_percentageChange)/100.0)

            else:
                randomNumber_percentageChange = random.random()/4.0
                priceObject.futPrice= priceObject.futPrice*(1+(randomNumber_priceUpDown*randomNumber_percentageChange)/100.0)


    def __getNextPrice(self, priceObject):
        """
        Fetches next timestamp price
        """
        randomNumber_priceUpDown = random.randrange(-1, 2, 2)
        randomNumber_Change = random.random()/20000.0
        if self.__lastPricepriceObject.futPrice>0:
            xCordinates = [self.__xIndex-1]+ self.__xCordinatesPriceLeft
            yCordinates = [self.__lastPricepriceObject.futPrice] + self.__priceMovementLeft
            pricePolyFit = np.polyfit(xCordinates[:2], yCordinates[:2], 1 , rcond = 2e-4)
            pricePolyFitFunction = np.poly1d(pricePolyFit)
            approxNextPrice = pricePolyFitFunction(self.__xIndex)
            priceObject.futPrice = approxNextPrice*(1 + randomNumber_priceUpDown*randomNumber_Change)
        else:
            priceObject.futPrice = self.__priceMovementLeft[0]
        if len(self.__priceMovementLeft)==0:
            pass
        elif self.__xIndex==self.__xCordinatesPriceLeft[0]:
            self.__priceMovementLeft = self.__priceMovementLeft[1:]
            self.__xCordinatesPriceLeft = self.__xCordinatesPriceLeft[1:]


    def runSimulator(self,priceObject):
        """
        Simulates price movement.
        """
        self.__getNextPrice(priceObject)
        self.__simulateDayOpenPrice(priceObject)
        self.__simulateIntradayPriceSpikes(priceObject)
        if priceObject.futPrice<0:
            priceObject.futPrice= self.__lastPricepriceObject.futPrice
        self.__lastPricepriceObject = priceObject
#                print priceObject.futPrice
        if self.__optionType=='Call' or self.__optionType=='Put':
            randomNumber_vix = 0.15 + random.randrange(-1, 2, 2)*random.random()/100.0
            time_left = self.startDaysLeft - self.__xIndex/22500.0
            priceObject.optionPrice = calc_premium(priceObject.futPrice, self.__optionType, self.symbolObj.strikePrice, time_left, vix=randomNumber_vix)
        else:
            priceObject.optionPrice = -1
        self.__xIndex+=1
