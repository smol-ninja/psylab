import pdb
from suds.client import Client
import mysql.connector
from mysql.connector.pooling import MySQLConnectionPool
from mysql.connector import errorcode
import re
import datetime
import time

from engine import settings
from engine.utilities.logger import get_logger
from engine.feedService.reportbyte import convert_to_report
from engine.exchangeclients.orderObject import OrderObject
from engine.utilities.utilities import get_months_list

MONTHS = get_months_list()

class Symphony(object):
    accountId = settings.get_account_id()
    username = settings.get_username()
    password = settings.get_password()

    def __init__(self):
        self.logger = get_logger(__name__)

        wsdlUrl = settings.get_url()
        self.client = Client(wsdlUrl)
        self.forced_logout()
        self.login_to_symphony_api()

    """Account related functions"""
    def login_to_symphony_api(self):
        try:
            self.client.service.loginToORS(prestoUser=self.username, prestoPasswd=self.password)
            print "Connected to Symphony Server and logged in\n"
            self.logger.info("Connected to Symphony Server and logged in")
        except Exception as err:
            self.logger.error(Exception(err))
            raise Exception(err)
        return 1

    def logout_from_symphony_api(self):
        try:
            self.client.service.logoutFromORS(prestoUser=self.username, prestoPasswd=self.password)
            print "Logged out successfully!"
            self.logger.info("Logged out successfully!")
        except Exception as err:
            self.logger.error(Exception(err))
            raise Exception(err)
        return 1

    def forced_logout(self):
        try:
            self.client.service.forceLogoutFromORS(prestoUser=self.username, prestoPasswd=self.password)
            print "Forced Logged out successfully!\n"
            self.logger.info("Forced Logged out successfully!")
        except Exception as err:
            self.logger.error(Exception(err))
            raise Exception(err)
        return 1

    def get_all_exchanges(self):
        try:
            return self.client.service.getAllExchanges()
        except Exception as err:
            self.logger.error(Exception(err))
            raise Exception(err)

    def get_symbol_list(self, exchange):
        try:
            return self.client.service.getSymbolsFromExAndSeg(exchange=exchange, segment='')
        except Exception as err:
            self.logger.error(Exception(err))
            raise Exception(err)

    def get_securityId(self, exchange, symbol):
        try:
            return self.client.service.getSecurityId(exchange=exchange, symbol=symbol, segment='')
        except Exception as err:
            self.logger.error(Exception(err))
            raise Exception(err)

    def get_symbol_details_for(self, exchange, securityId):
        try:
            symbolDetail = self.client.service.getSymbolDetail(exchange=exchange, securityID=securityId)
            return symbolDetail
        except Exception as err:
            self.logger.error(Exception(err))
            raise Exception(err)

    def get_symbol_details_instrumenttype(self, exchange, instrumentType):
        try:
            symbolDetail = self.client.service.scriptsForExchangeInstrType(exchange=exchange, instrument_type=instrumentType)
            return symbolDetail
        except Exception as err:
            self.logger.error(Exception(err))
            raise Exception(err)

    def get_brokers_list(self):
        try:
            return self.client.service.getAvailableBrokers()
        except Exception as err:
            self.logger.error(Exception(err))
            self.logger.warning("will retry after 30 seconds")
            time.sleep(30)
            self.get_brokers_list()

    def check_connection(self):
        try:
            self.client.service.getConnectionStatus(prestoUser=self.username)
            return True
        except Exception as err:
            self.logger.critical(err)
            self.logger.info("Session error, trying to Login")
            self.forced_logout()
            self.login_to_symphony_api()
            self.check_connection()

    def place_order(self, algoId, securityId, symbol, optionType, strikePrice, side, quantity, expiryMonthYear, price, securityType, conn, cur, orderType='Limit', stopPrice=None):
        # creating order object type using wsdl factory method
        self.logger.info("creating orders object for %s" % (algoId, ))
        orderObject = self.client.factory.create('esbOrder')

        # user and account details
        orderObject.esbuser = self.username
        orderObject.esbaccount = self.accountId

        # exchange details
        brokers_list = self.get_brokers_list()
        if len(brokers_list) == 0:
            self.logger.critical("NO BROKERS ARE AVAILABLE. PLEASE CONTACT SYMPHONY")

        for broker in brokers_list:
            if securityType in ['OPTION', 'FUTURE'] and bool(re.search('nsefo', broker)):
                orderObject.esbexchange = broker
                break

            elif securityType in ['STOCK', 'INDEX'] and bool(re.search('nsecm', broker)):
                orderObject.esbexchange = broker
                break

            elif securityType not in ['OPTION', 'FUTURE', 'STOCK', 'INDEX']:
                self.logger.error("WHAT THE FUCK! INVALID SECURITY TYPE. PLEASE BE CAREFUL")
                break

            elif not bool(re.search('nsefo', broker)) or not bool(re.search('nsecm', broker)):
                self.logger.error("INVALID BROKER. PLEASE CHECK. AVAILABLE BROKERS ARE %s" % (str(self.get_brokers_list())))

        # Contract details
        orderObject.securityID = securityId
        orderObject.esbsymbol = symbol
        if strikePrice is not None:
            orderObject.strikePrice = strikePrice

        orderObject.esbexpiry = self.get_expiry_date(securityId, expiryMonthYear, conn, cur)
        orderObject.esbsecurityType = securityType

        # order details
        orderObject.esborderType = orderType
        if stopPrice is not None:
            orderObject.esbstopPrice = stopPrice
        orderObject.esbprice = price
        orderObject.esbquantity = quantity
        orderObject.esbside = side
        orderObject.esbtimeInForce = 'Day'
        if optionType is not None:
            orderObject.optionType = optionType
        orderObject.isManualOrder = 0

        self.logger.info(orderObject)

        try:
            orderId = self.client.service.placeOrder(prestoUser=self.username, orderSingle=orderObject)
        except Exception as err:
            self.logger.error(Exception(err))

        return orderId

    def replace_order(self, orderId=None, quantity=None, price=None, orderType=None, stopPrice=None):
        try:
            orderId = self.client.service.replaceOrder(prestoUser=self.username, clientOrderId=orderId, newQty=quantity, newPrice=price, newOrdType=orderType, newStopPx=stopPrice)
            return orderId
        except Exception as err:
            self.logger.error(Exception(err))
            self.logger.warning("will retry after 30 seconds")
            time.sleep(30)
            self.replace_order(orderId, quantity, price, orderType, stopPrice)

    def get_expiry_date(self, securityId, expiryMonthYear, conn, cur):
        query = "SELECT `expiryDay` FROM `symbols` WHERE `securityId`=%s" % (securityId)
        cur.execute(query)
        result = cur.fetchone()
        expiryDay = result[0]
        if len(expiryDay) == 1:
            expiryDay = '0' + expiryDay

        expiryMonth = "".join(re.findall("[a-zA-Z]", expiryMonthYear))
        for mi in range(12):
            if expiryMonth.lower() in MONTHS[mi]:
                expiryMonthIndex = mi + 1
                if len(str(expiryMonthIndex)) == 1:
                    expiryMonthIndex = '0' + str(expiryMonthIndex)
                else:
                    expiryMonthIndex = str(expiryMonthIndex)
                break

        expiryMonth = expiryMonthIndex

        expiryYear = "".join(re.findall("[0-9]", expiryMonthYear))
        if len(expiryYear) == 2:
            expiryYear = "20" + expiryYear


        expiryDateTime = "%s-%s-%s" % (expiryYear, expiryMonth, expiryDay)

        return expiryDateTime

    def get_opt_security_id(self, symbol, opType, strikePrice, expiryMonthYear, securityType, conn, cur):
        if securityType == "OPTION":
            query = "SELECT `strikePrice` FROM `symbols` WHERE `symbol`=%s AND `optionType`=%s AND `expiryMonthYear`=%s"
            qargs = (symbol, opType, expiryMonthYear)
            cur.execute(query, qargs)
            recordedStrikePrices = cur.fetchall()
            strikePrice = min(recordedStrikePrices, key=lambda x: abs(float(x[0])-float(strikePrice)))
            strikePrice = strikePrice[0]

            query = "SELECT `securityId` FROM `symbols` WHERE `symbol`=%s AND `optionType`=%s AND `expiryMonthYear`=%s AND `strikePrice`=%s"
            qargs = (symbol, opType, expiryMonthYear, int(strikePrice))
        elif securityType == "FUTURE":
            query = "SELECT `securityId` FROM `symbols` WHERE `symbol`=%s AND `expiryMonthYear`=%s AND (`instrumentType`='FUTIDX' OR `instrumentType`='FUTSTK')"
            qargs = (symbol, expiryMonthYear)

        cur.execute(query, qargs)
        result = cur.fetchone()
        securityId = result[0]

        return securityId, strikePrice

    def update_order_details(self, algoId, orderId, securityId, side, quantity, price, conn, cur):
        orderStatus = 'placed'

        query = "SELECT `lotsize` FROM `symbols` WHERE `securityId`=%s"
        qargs = (securityId, )
        cur.execute(query, qargs)
        result = cur.fetchone()
        lotsize = result[0]
        orderValue = float(price)*int(quantity)*int(lotsize)

        query = "INSERT INTO `orders` (`orderId`, `originalOrderId`, `orderSecurityId`, `orderstatus`, `algoid`, `side`, `price`, `quantity`, `value`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        qargs = (str(orderId), str(orderId), str(securityId), str(orderStatus), str(algoId), str(side), float(price), int(quantity), float(orderValue))

        try:
            cur.execute(query, qargs)
            conn.commit()
        except Exception as err:
            self.logger.error(Exception(err))

    def get_trade_history_report(self):
        getTradeHistoryResponse = self.client.service.getTradedHistoryFormated(prestoUser=self.username)
        reportHolder = []
        for oo in getTradeHistoryResponse:
            reportHolder.append(convert_to_report(oo))
        return reportHolder

    def get_all_open_orders(self):
        try:
            getOpenOrdersResponse = self.client.service.getOpenOrdersFormated(prestoUser=self.username)
            reportHolder = []
            for oo in getOpenOrdersResponse:
                reportHolder.append(convert_to_report(oo))
            return reportHolder
        except Exception as err:
            self.logger.error(Exception(err))

    def get_open_orders_for_id(self, orderId):
        try:
            getOpenOrdersResponse = self.client.service.getOpenOrdersFormatedForClientOrderID(prestoUser=self.username, clientOrderID=orderId)
            reportHolder = convert_to_report(getOpenOrdersResponse)
            return reportHolder
        except Exception as err:
            self.logger.error(Exception(err))
            self.logger.warning("will retry after 30 seconds")
            time.sleep(30)
            self.get_open_orders_for_id(orderId)

    def get_order_details(self, orderId):
        try:
            response = self.client.service.getLastTradeHistoryFormatedForClientOrderID(prestoUser=self.username, clientOrderID=orderId)
            report = convert_to_report(response)
            return report
        except Exception as err:
            self.logger.error(Exception(err))
            self.logger.warning("will retry after 30 seconds")
            time.sleep(30)
            self.get_order_details(orderId)

    def square_off_positions(self, algoId, conn, cur, symbol="all"):
        tradedSecurities = []
        orderObject = []
        today_date = datetime.datetime.today().strftime('%Y-%m-%d')

        query = "SELECT `orderSecurityId` FROM `orders` WHERE `algoid`=%s"
        qargs = (algoId,)
        cur.execute(query, qargs)
        orderSecuritiesIds = cur.fetchall()

        for secId in orderSecuritiesIds:
            if symbol != "all":
                query = "SELECT `symbol` FROM `symbols` WHERE `securityId`=%s"
                qargs = secId
                cur.execute(query, qargs)
                result = cur.fetchone()
                if result[0].lower() == symbol.lower() and secId[0] not in tradedSecurities:
                    tradedSecurities.append(secId[0])
            else:
                if secId[0] not in tradedSecurities:
                    tradedSecurities.append(secId[0])

        for secId in tradedSecurities:
            query = "SELECT * FROM `symbols` WHERE `securityId`={}".format(secId)
            cur.execute(query)
            result = cur.fetchone()
            symbol = result[1]
            securityType = result[5]
            strikePrice = result[8]
            optionType = result[7]
            expiryMonthYear = result[11]

            query = "SELECT sum(`quantity`) FROM `orders` WHERE `orderSecurityId`=%s AND `side`=%s AND `algoid`=%s"
            qargs = (secId,'Buy', algoId)
            cur.execute(query, qargs)
            result = cur.fetchone()

            totalBuyQuantities = 0
            if result[0] is not None:
                totalBuyQuantities = result[0]

            qargs = (secId,'Sell', algoId)
            cur.execute(query, qargs)
            result = cur.fetchone()

            totalSellQuantities = 0
            if result[0] is not None:
                totalSellQuantities = result[0]

            difference = int(totalBuyQuantities) - int(totalSellQuantities)
            if securityType == 'FUTIDX' or securityType == "FUTSTK":
                if difference > 0:
                    orderObject.append(OrderObject(symbol=symbol, securityType="FUTURE", side='Sell', expiryMonthYear=expiryMonthYear, quantity=difference))
                elif difference < 0:
                    orderObject.append(OrderObject(symbol=symbol, securityType="FUTURE", side='Buy', expiryMonthYear=expiryMonthYear, quantity=-difference))
            elif securityType == 'OPTIDX' or securityType == 'OPTSTK':
                if difference > 0:
                    orderObject.append(OrderObject(symbol=symbol, optionType=optionType, strikePrice=strikePrice, side='Sell', expiryMonthYear=expiryMonthYear, quantity=difference))
                elif difference < 0:
                    orderObject.append(OrderObject(symbol=symbol, optionType=optionType, strikePrice=strikePrice, side='Buy', expiryMonthYear=expiryMonthYear, quantity=-difference))

        return orderObject
