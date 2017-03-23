"""
This is a template algorithm to understand the functions

1. context
Use 'context' to assign a global variable. Usage: you can assign context.strikePrice = 8900 and retrieve the strikepirce at any place in the algorithm using context.strikeprice.

2. sid
Call this function to fetch security Id of a security.
Usage: sid(symbol, securitytype, expiry=None, strikeprice=None, optiontype=None)

"""

from psylib.pipeline import *
from psylib.algorithm import *

def initialize(psy):
    """
    Called once everyday before the algorithm begins
    """
    context.beginTime = "9:20"
    context.endTime = "15:20"
    context.nifty = sid(symbol='nifty', securitytype='future', expiry='current')

    return

def algo_begins(psy):
    """
    Called once as soon as time hits beginTime (or market starts if
    beginTime is missing)
    """
    price = fetch_price(context.nifty)
    context.put = sid(symbol='nifty', securitytype='option', strikeprice=price, optiontype='put', expiry='current')
    context.call = sid(symbol='nifty', securitytype='option', strikeprice=price, optiontype='call', expiry='current')

    place_order(sid=context.call, order="limit", quantity="1200", side="sell")
    place_order(sid=context.put, order="limit", quantity="1200", side="sell")
    context.callSellPrice = fetch_price(context.call)
    context.putSellPrice = fetch_price(context.put)

    return

def algo_handle(psy, factor=1):
    """
    Called every `factor` seconds
    Your main logic will go here
    """
    callPrice = fetch_price(context.call)
    putPrice = fetch_price(context.put)

    if abs(callPrice - context.callSellPrice) >= 0.05*context.callSellPrice:
        square_off_positions(context.call)

    if abs(putPrice - context.putSellPrice) >= 0.05*context.putSellPrice:
        square_off_positions(context.put)

    return

def algo_ends(psy):
    """
    Called once as soon as time hits endTime (or market ends
    if endTime is missing)
    """
    square_off_positions(context.call)
    square_off_positions(context.put)

    return

def after_market(psy):
    """
    Called once after the market ends
    """

    return

while 1:
    print "Its working"
