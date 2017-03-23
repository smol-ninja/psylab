import json
import pika

from engine.errors import (
    OrderQuantityError,
    SideError,
    OrderTypeError,
    SidError,
    OrderPriceError
    )
from engine import constants

class OrderObject(object):
    """
    Create Order object to be procesed further.
    Validates the parameter.
    """
    def __init__(self, user, algo, sid, side, quantity, orderType='limit'):
        self._user = user
        self._algo = algo
        self._sid = sid
        self._side = side
        self._quantity = quantity
        self._orderType = orderType
        self._is_valid_order()

    @property
    def user(self):
        return self._user

    @property
    def algo(self):
        return self._algo

    @property
    def sid(self):
        return self._sid

    @property
    def side(self):
        return self._side

    @property
    def quantity(self):
        return self._quantity

    @property
    def orderType(self):
        return self._orderType

    @orderType.setter
    def orderType(self, value):
        self._orderType = value
        self._is_valid_orderType()

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
        self._is_valid_price()

    def _is_valid_order(self):
        if self._is_valid_orderType() and self._is_valid_side() and self._is_valid_quantity() and self._is_valid_sid():
            return True

    def is_valid_sid(self):
        # To be done using database queries
        return True

    def _is_valid_quantity(self):
        if type(self._quantity) != int or self._quantity < 1:
            raise OrderQuantityError(quantity=self._quantity, sid=self._sid)

    def _is_valid_side(self):
        if self._side.lower() not in constants.SIDE:
            raise SideError(side=self._side, sid=self._sid)

    def _is_valid_orderType(self):
        if self._orderType.lower() not in constants.ORDER_TYPE:
            raise OrderTypeError(orderType=self._orderType, sid=self._sid)

    def _is_valid_price(self):
        if type(self._price) != 'float' or self._price < 0:
            raise OrderPriceError(sid=self._sid, orderPrice=self._price)
