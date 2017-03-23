"""
Functions to support algorithms building
"""

from psylab.pipeline import *

def sid(symbol, securitytype, expiry=None, strikeprice=None, optiontype=None):
    """
    Returns the security ID for the given input params
    """
    is_valid_security(symbol, securitytype, expiry, strikeprice, optiontype)
