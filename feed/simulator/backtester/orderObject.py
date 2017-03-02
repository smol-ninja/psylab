# -*- coding: utf-8 -*-
"""
Created on Thu Feb 02 18:13:14 2017

@author: sagar
"""

class OrderObject(object):
    def __init__(self, symbol, side, quantity, strikePrice=None, optionType=None):
        self.symbol = symbol
        self.side = side
        self.optionType = optionType
        self.strikePrice = strikePrice
        self.quantity = quantity
