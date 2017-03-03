"""
This is a template algorithm to understand the functions

1. psy
Use 'psy' to assign a global variable. Usage: you can assign psy.strikePrice = 8900 and retrieve the strikepirce at any place in the algorithm using psy.strikeprice.

2. sid
Call this function to fetch security Id of a security.
Usage: sid(symbol, securitytype, expiry=None, strikeprice=None, optiontype=None)

"""

from psylab.pipeline import *
from psylab.algorithm import *

def initialize(psy):
    """
    Called once everyday before the algorithm begins
    """
    psy.beginTime = "9:20"
    psy.endTime = "15:20"
    psy.nifty = sid(symbol='nifty', securitytype='future', expiry='current')

    return

def algo_begins(psy):
    """
    Called once as soon as time hits beginTime (or market starts if
    beginTime is missing)
    """
    price = fetch_price(psy.nifty)
    psy.put = sid(symbol='nifty', securitytype='option', strikeprice=price, optiontype='put', expiry='current')
    psy.call = sid(symbol='nifty', securitytype='option', strikeprice=price, optiontype='call', expiry='current')

    place_order(sid=psy.call, order="limit", quantity="1200", side="sell")
    place_order(sid=psy.put, order="limit", quantity="1200", side="sell")
    psy.callSellPrice = fetch_price(psy.call)
    psy.putSellPrice = fetch_price(psy.put)

    return

def algo_handle(psy, factor=1):
    """
    Called every `factor` seconds
    Your main logic will go here
    """
    callPrice = fetch_price(psy.call)
    putPrice = fetch_price(psy.put)

    if abs(callPrice - psy.callSellPrice) >= 0.05*psy.callSellPrice:
        square_off_positions(psy.call)

    if abs(putPrice - psy.putSellPrice) >= 0.05*psy.putSellPrice:
        square_off_positions(psy.put)

    return

def algo_ends(psy):
    """
    Called once as soon as time hits endTime (or market ends
    if endTime is missing)
    """
    square_off_positions(psy.call)
    square_off_positions(psy.put)

    return

def after_market(psy):
    """
    Called once after the market ends
    """

    return
