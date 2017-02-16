                              # -*- coding: utf-8 -*-
"""
Created on Thu Jul 07 02:57:53 2016

@author: Sagar
"""

from scipy import stats
import math
def black_scholes (cp, s, k, t, v, rf=0.032, div=0):
        """ Price an option using the Black-Scholes model.
        s: initial stock price
        k: strike price
        t: expiration time
        v: volatility
        rf: risk-free rate
        div: dividend
        cp: +1/-1 for call/put
        """
        t = float(t)/365.0
        d1 = (math.log(s/k)+(rf-div+0.5*math.pow(v,2))*t)/(v*math.sqrt(t))
        d2 = d1 - v*math.sqrt(t)
        optprice = (cp*s*math.exp(-div*t)*stats.norm.cdf(cp*d1)) - (cp*k*math.exp(-rf*t)*stats.norm.cdf(cp*d2))
        return optprice
    
def calc_premium(underlyingValue,callPut,strikePrice,daysToExpiry,vix=0.15):
        """
        calc_premium(underlyingValue,callPut,strike,daysToExpiry,vix=0.15)
        callPut syntax :
            'Call'
            'Put'
        return optionPrice
        """    
        if callPut=='Call':            
            return black_scholes(1,underlyingValue,float(strikePrice),daysToExpiry,vix)  
        elif callPut=='Put':
            return strikePrice - underlyingValue + black_scholes(1,underlyingValue,float(strikePrice),daysToExpiry,vix)  
        else:
            print 'Enter Call or Put'
            return -1
            