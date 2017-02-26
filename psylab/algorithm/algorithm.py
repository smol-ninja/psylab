"""
functions to support algorithms building
"""

from psylab.pipeline import *

class Psy(object):
    pass

def sid(symbol, securitytype, expiry=None, strikeprice=None, optiontype=None):
    is_valid_security(symbol, securitytype, expiry, strikeprice, optiontype)
