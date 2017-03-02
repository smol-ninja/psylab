"""
Constants used in the project are defined here
"""

SECURITY_TYPES = ['option', 'future', 'equity']
EXPIRY = ['previous', 'current', 'next']
OPTION_TYPES = ['call', 'put']

DATA_TYPE = {
    'expiry': str,
    'symbol': str,
    'securitytype': str,
    'strikeprice': float,
    'optiontype': str,
}
