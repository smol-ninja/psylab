import struct
import socket

from engine.live_manager import settings

class Ticker(object):
    messageSize = None
    broadcastMessageHeader = None
    reserved1 = None
    reserved2 = None
    reserved3 = None
    reserved4 = None
    indexFlag = None

    instrumentIdentifier = None

    totalQuantity = None
    lastTradedPrice = None
    lastTradedQuantity = None
    lastTradeTime = None
    averageTradedPrice = None

    orderByPriceBuy = None
    orderByPriceSell = None

    totalBuyQuantity = None
    totalSellQuantity = None

    closePrice = None
    openPrice = None
    highPrice = None
    lowPrice = None

    openInterestDetails = None
    totalTrades = None
    highestPriceEver = None
    lowestPriceEver = None
    totalTradedValue = None

    class BroadcastMessageHeader(object):
        exchangeTimeStamp = None
        messageCode = None
        messageSize = None

        reserved1 = None
        reserved2 = None
        reserved3 = None

    class OrderByPrice(object):
        quantity = None
        orderPrice = None
        totalNumberOfOrders = None
        reserved = None

    class OpenInterestDetails(object):
        currentOpenInterest = None

class Extractor(object):
    sizeOfBCHeader = 21
    sizeOfOBP = 14
    sizeOfOpenID = 4

    def set_buffer(self, ba, start):
        self.startPos = start
        self.bytebuffer = bytearray(ba)

    def fill_market_picture(self):
        pos = self.startPos
        mp = Ticker()

        mp.messageSize = self._retrieve_char_array(pos, 5)
        pos += 5
        mp.BroadcastMessageHeader = self._fill_bcast_header(pos)
        pos += self.sizeOfBCHeader
        # mp.reserved1 = struct.unpack('b', self.bytebuffer[pos])[0]
        pos += 1
        mp.instrumentIdentifier = struct.unpack('<i', self.bytebuffer[pos : pos+4])[0]
        pos += 4

        # mp.reserved2 = struct.unpack('c', self.bytebuffer[pos])[0]
        pos += 1
        # mp.indexFlag = struct.unpack('c', self.bytebuffer[pos])[0]
        pos += 1
        mp.totalQuantity = struct.unpack('<i', self.bytebuffer[pos : pos+4])[0]
        pos += 4
        lastTradedPriceInPaise = struct.unpack('<i', self.bytebuffer[pos : pos+4])[0]
        mp.lastTradedPrice = lastTradedPriceInPaise/100.0
        pos += 4
        mp.lastTradedQuantity = struct.unpack('<i', self.bytebuffer[pos : pos+4])[0]
        pos += 4
        mp.lastTradeTime = struct.unpack('<i', self.bytebuffer[pos : pos+4])[0]
        pos += 4
        averageTradedPriceInPaise = struct.unpack('<i', self.bytebuffer[pos : pos+4])[0]
        mp.averageTradedPrice = averageTradedPriceInPaise/100.0
        pos += 4

        mp.orderByPriceBuy = self._get_mp_array(pos, 5)
        pos += 5*self.sizeOfOBP
        mp.orderByPriceSell = self._get_mp_array(pos, 5)
        pos += 5*self.sizeOfOBP

        mp.totalBuyQuantity = struct.unpack('<q', self.bytebuffer[pos : pos+8])[0]
        pos += 8
        mp.totalSellQuantity = struct.unpack('<q', self.bytebuffer[pos : pos+8])[0]
        pos += 8
        mp.reserved3 = self._retrieve_char_array(pos, 2)
        pos += 2
        closePriceInPaise = struct.unpack('<i', self.bytebuffer[pos : pos+4])[0]
        mp.closePrice = closePriceInPaise/100.0
        pos += 4
        openPriceInPaise = struct.unpack('<i', self.bytebuffer[pos : pos+4])[0]
        mp.openPrice = openPriceInPaise/100.0
        pos += 4
        highPriceInPaise = struct.unpack('<i', self.bytebuffer[pos : pos+4])[0]
        mp.highPrice = highPriceInPaise/100.0
        pos += 4
        lowPriceInPaise = struct.unpack('<i', self.bytebuffer[pos : pos+4])[0]
        mp.lowPrice = lowPriceInPaise/100.0
        pos += 4

        mp.reserved4 = struct.unpack('<h', self.bytebuffer[pos : pos+2])[0]
        pos += 2

        mp.openInterestDetails = self._fill_open_interest(pos)
        pos += self.sizeOfOpenID
        mp.totalTrades = struct.unpack('<i', self.bytebuffer[pos : pos+4])[0]
        pos += 4
        highestPriceEverInPaise = struct.unpack('<i', self.bytebuffer[pos : pos+4])[0]
        mp.highestPriceEver = highestPriceEverInPaise/100.0
        pos += 4
        lowestPriceEverInPaise = struct.unpack('<i', self.bytebuffer[pos : pos+4])[0]
        mp.lowestPriceEver = lowestPriceEverInPaise/100.0
        pos += 4
        mp.totalTradedValue = struct.unpack('<d', self.bytebuffer[pos : pos+8])[0]
        pos += 8

        return mp

    def _retrieve_char_array(self, pos, length):
        i = 0
        val = ''

        for i in range(length):
            # val += struct.unpack('c', str(self.bytebuffer[pos + i]))[0]
            continue
        return val

    def _fill_bcast_header(self, pos):
        bmh = Ticker.BroadcastMessageHeader()

        bmh.exchangeTimeStamp = struct.unpack('<i', self.bytebuffer[pos : pos+4])[0]
        pos += 4
        bmh.messageCode = struct.unpack('<h', self.bytebuffer[pos : pos+2])[0]
        pos += 2
        bmh.reserved1 = struct.unpack('<h', self.bytebuffer[pos : pos+2])[0]
        pos += 2
        bmh.reserved2 = self._retrieve_char_array(pos, 9)
        pos += 9
        bmh.messageSize = struct.unpack('<h', self.bytebuffer[pos : pos+2])[0]
        pos += 2
        bmh.reserved3 = struct.unpack('<h', self.bytebuffer[pos : pos+2])[0]

        return bmh

    def _get_mp_array(self, pos, arraySize):
        obpa = []
        for i in range(arraySize):
            obpa.append(self._fill_order_by_price(pos + i*self.sizeOfOBP))
        return obpa

    def _fill_order_by_price(self, pos):
        obp = Ticker.OrderByPrice()
        obp.quantity = struct.unpack('<i', self.bytebuffer[pos : pos+4])[0]
        pos += 4
        orderPriceInPaise = struct.unpack('<i', self.bytebuffer[pos : pos+4])[0]
        obp.orderPrice = orderPriceInPaise/100.0
        pos += 4
        obp.totalNumberOfOrders = struct.unpack('<i', self.bytebuffer[pos : pos+4])[0]
        pos += 4
        obp.reserved = struct.unpack('<h', self.bytebuffer[pos : pos+2])[0]

        return obp

    def _fill_open_interest(self, pos):
        oid = Ticker.OpenInterestDetails()
        oid.currentOpenInterest = struct.unpack('<i', self.bytebuffer[pos : pos+4])[0]

        return oid

def _udp_socket():
    mcastGroup = settings.get_mcast_group()
    mcastPort = settings.get_mcast_port()
    localIp = settings.get_localIp()

    # Create the datagram socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

    # SO_REUSEADDR flag tells the kernel to reuse a local socket
    # in TIME_WAIT state, without waiting for its natural timeout to expire
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind to the server address
    server_address = (localIp, mcastPort)
    sock.bind(server_address)

    # Tell the OS to add the socket to the multicast group
    group = socket.inet_aton(mcastGroup)
    mreq = struct.pack('4sl', group, socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    return sock

def _fetch_data(sid, fetch='price'):
    sock = _udp_socket()
    extractor = Extractor()
    while True:
        data, address = sock.recvfrom(8192)
        extractor.set_buffer(data, 0)
        ticker = extractor.fill_market_picture()
        instrumentId = str(ticker.instrumentIdentifier)
        if instrumentId == sid:
            if fetch == 'price':
                return float(ticker.lastTradedPrice)
            elif fetch == 'volume':
                return int(ticker.lastTradedQuantity)
            elif fetch == 'open-interest':
                return int(ticker.openInterestDetails.currentOpenInterest)
            elif fetch == "object":
                return ticker

def fetch_price(sid):
    return _fetch_data(sid, 'price')

def fetch_quantity(sid):
    return _fetch_data(sid, 'volume')

def fetch_open_interest(sid):
    return _fetch_data(sid, 'open-interest')

def fetch_ticker(sid):
    return _fetch_data(sid, 'object')
