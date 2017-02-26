"""
This is a template algorithm to understand the functions
"""

from psylab.pipeline import *
from psylab.algorithm import *

sid(symbol='icici', securitytype='option', expiry='current', strikeprice=1210, optiontype='call')

def initialize(psy):
    """
    Called once everyday before the algorithm begins
    """
    icici = sid(symbol='icici', securitytype='option', expiry='current', strikeprice=1210, optiontype='call')
    nifty = sid(symbol='nifty', securitytype='future', expiry='next')
    itc = sid(symbol='itc', securitytype='equity')
    return

def after_market(psy):
    """
    Called once everyday after the algorithm ends
    return
    """

def handle_data(psy):
    """
    Called every minute
    """
    return
