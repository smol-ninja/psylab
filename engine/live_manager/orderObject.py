# from feed.nse import fetch_price
from engine.logger import get_logger
import json
import pika

"""
call OrderValidation function and return the output to json_to_object function
"""

class OrderObject(object):
    logger=get_logger(__name__)
    def __init__(self, sid, side, quantity, orderType='limit', stopPrice=None, price=None):
        self.sid = sid
        self.side = side
        self.quantity = quantity
        self.orderType = orderType
        self.stopPrice = stopPrice
        self.price = price
        self.valid=OrderValidation().validation(self)
    def get_value(self):
        return self.valid
"""
1. Validate order parameters and return boolean value
2. Create a log file if something went wrong
"""
class OrderValidation(object):
    def _side_validation(self):
        if self.orderObj.side is None:
            self.orderObj.logger.error('Side can not be None')
            raise Exception('Side can not be None')
        else:
            if self.orderObj.side.lower()=='buy' or self.orderObj.side.lower()=='sell':
                return True
            else:
                self.orderObj.logger.error('Incorrect side type')
                raise Exception('Incorrect side type')
    def _quantity_validation(self):
        if self.orderObj.quantity is None:
            self.orderObj.logger.error('Quantity can not be None')
            raise Exception('Quantity can not be None')
        else:
            try:
                int(self.orderObj.quantity)
                return True
            except ValueError:
                self.orderObj.logger.error('Incorrect Quantity type')
                raise Exception('Incorrect Quantity type')
    def _sid_validation(self):
        # TODO: Need to implement side validation
        return True
    def _order_validation(self):
        if self.orderObj.orderType is None:
            self.orderObj.logger.error('Order type can not be None')
            raise Exception('Order type can not be None')
        else:
            if self.orderObj.orderType.lower()=='limit' or self.orderObj.orderType.lower()=='market':
                return True
            else:
                self.orderObj.logger.error('Incorrect order type')
                raise Exception('Incorrect order type')
    def validation(self,orderObj):
        self.orderObj=orderObj
        if self._order_validation() and self._side_validation and self._quantity_validation() and self._sid_validation():
            if self.orderObj.orderType.lower()=='market':
                self.orderObj.logger.info('orderType:Market, Order placed')
            else:
                pass
                # TODO: fetch_price function
                # self.price=fetch_price(self.sid)
            return True
        else:
            return False

"""
Get objects from rabbitMQ queue
"""
def obj_consumer():
    HEARTBEAT_INTERVAL=2
    conn_params = pika.ConnectionParameters(
            heartbeat_interval=HEARTBEAT_INTERVAL
        )
    connection = pika.BlockingConnection(conn_params)
    channel = connection.channel()
    for method_frame, properties, body in channel.consume('hello'):
        json_to_object(body)
    # Cancel the consumer and return any pending objects
    requeued_messages = channel.cancel()
    print('Requeued %i messages' % requeued_messages)
    connection.close()
"""
Decoding json to object
"""
def json_to_object(body):
    js=json.loads(body)
    orderObj=OrderObject(js["sid"],js["side"],js["quantity"],js["orderType"],js["price"])
    if orderObj.get_value():
        print 'write date'
    else:
        print 'retry'
obj_consumer()
