"""
Functions supporting pipeline functionality
"""

from engine.constants import (
    SECURITY_TYPES,
    EXPIRY,
    OPTION_TYPES,
    DATA_TYPE,
    )
from feed.nse import fetch_price_nse, fetch_open_interest_nse, fetch_quantity_nse

def is_valid_security(symbol, securitytype, expiry=None, strikeprice=None, optiontype=None):
    """
    Checks datetypes for input parameters. Raises error if invalid types found.
    """
    if securitytype not in SECURITY_TYPES:
        raise ValueError('Invalid value for securitytype. Available values: %s' % (SECURITY_TYPES, ))

    else:
        if type(symbol) != DATA_TYPE['symbol']:
            raise TypeError('Invalid %s for symbol. Expected: %s' % (type(symbol), DATA_TYPE['symbol']))
        if securitytype in ['future', 'option']:
            if expiry not in EXPIRY:
                raise ValueError('Invalid value for expiry. Available values: %s' % (EXPIRY, ))

        if securitytype in ['option']:
            if optiontype not in OPTION_TYPES:
                raise ValueError('Invalid value for optiontype. Available values: %s' % (OPTION_TYPES, ))

            try:
                strikeprice = float(strikeprice)
            except:
                raise ValueError('Invalid %s for strikeprice. Expected %s' % (type(strikeprice), DATA_TYPE['strikeprice']))

    return True

def fetch_price(security):
    """
    Fetches the last traded price for the given security
    """
    return fetch_price_nse(security)

def fetch_quantity(security):
    """
    Fetches the last traded quantity for the given security
    """
    return fetch_quantity_nse(security)

def fetch_open_interest(security):
    """
    Fetches the last traded quantity for the given security
    """
    return fetch_open_interest_nse(security)
