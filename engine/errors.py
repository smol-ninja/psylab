class PsylabError(Exception):
    msg = None

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def __str__(self):
        msg = self.msg.format(**self.kwargs)
        return msg

    __unicode__ = __str__
    __repr__ = __str__

class OrderQuantityError(PsylabError):
    msg = "Invalid order quantity: {quantity} for security ID: {sid}"

class SideError(PsylabError):
    msg = "Invalid {side} side for security ID: {sid}. Available values: buy, sell"

class SidError(PsylabError):
    msg = "{sid} is not a valid security Id"

class OrderTypeError(PsylabError):
    msg = "Not a valid orderType: {orderType} for security ID: {sid}"

class OrderPriceError(PsylabError):
    msg = "OrderPrice: {OrderPrice} not allowed for security ID: {sid}"
