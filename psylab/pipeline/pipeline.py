"""
classes and functions supporting pipeline functionality
"""

from engine.constants import *

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
