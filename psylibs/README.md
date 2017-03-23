************************************************
*********** Functional Definitons **************
************************************************

1. context
Use 'context' to assign a globall variable. Usage: you can assign context.strikePrice = 8900 and retrieve the strikepirce at any place in the algorithm using context.strikeprice.

2. sid
Call this function to fetch security Id of a security.
Usage: sid(symbol, securitytype, expiry=None, strikeprice=None, optiontype=None)
