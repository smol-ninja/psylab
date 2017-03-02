************************************************
*********** Functional Definitons **************
************************************************

1. psy
Use 'psy' to assign a globall variable. Usage: you can assign psy.strikePrice = 8900 and retrieve the strikepirce at any place in the algorithm using psy.strikeprice.

2. sid
Call this function to fetch security Id of a security.
Usage: sid(symbol, securitytype, expiry=None, strikeprice=None, optiontype=None)
