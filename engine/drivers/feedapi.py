#!/usr/bin/env python

from pymongo import MongoClient
import datetime, dateutil.parser

# import time
# start_time = time.time()
client = MongoClient()
db = client.tickdata

def fetch_secId(symbol, securityType='stock', optionType=None, strikePrice=None, expiry=None):
    """
    securityType can be stock, futures or option.
    optionType can be call or put
    should return securityId
    expiry: DD-MM-YYYY
    """
    if securityType=='futures':
        if expiry=='current':
            symbol=symbol+'-I'
        elif expiry=='next':
            symbol=symbol+'-II'
        result=db.symbol_sid.find_one({'symbol':symbol})
    return result

def fetch_price(secId, datetime, frequency):
    """
	Take securityid and datetime as input.
    Use "YYYY-MM-DDTHH:MM:SS" format for datetime
    (SS) should be 59 for each case
    return close_price at the moment
	case 1: frequency=minute. fetch price at that minute
	case 2: freq = daily. fetch price on that day at 15:30
	case 3: freq = hourly, fetch price during that hour at closing. Example, 9:15, 10:15, 11:15
	case 4: freq = weekly, fetch price on every monday at 15:30
    """
    return fetch_data(secId, datetime, frequency,'closeValue')

def fetch_data(secId, datetime, frequency, objectType="closeValue"):
    """
	a generalized fucntion which can take "close_price"
	"open_price", "quantity", "open-interest" as type values.
	By default type="close_price"
    dateformat: "YYYY-MM-DDTHH:MM:SS"
    """
    d = dateutil.parser.parse(datetime)
    secid=str(secId)
    dateValue=str(d.strftime('%d%m%Y'))
    cursor=db.ticker.find_one({"_id":secid})
    if frequency=='minute':
        timeValue=str(d.strftime('%H%M%S'))
        try:
            obj=cursor['ticker'][dateValue][timeValue]
            return obj['closeValue']
        except Exception as e:
            pass
    elif frequency=='daily':
        timeValue='152959'
        try:
            obj=cursor['ticker'][dateValue][timeValue]
            return obj['closeValue']
        except Exception as e:
            pass
    elif frequency=='hourly':
        timeValue=str(d.strftime('%H'))
        timeValue=timeValue+'1559'
        try:
            obj=cursor['ticker'][dateValue][timeValue]
            return obj['closeValue']
        except Exception as e:
            pass
    # TODO: weekly

def fetch_price_list(secId, datefrom, dateto, frequency, dataType='array'):
    """
    a generalized fucntion which return all the close price
    from-to period
    dateformat: "YYYY-MM-DD"
    """
    return fetch_data_list(secId, datefrom, dateto, frequency,'closeValue', 'array')


def fetch_data_list(secId, datefrom, dateto, frequency, objectType="closeValue", dataType='array'):
    """
	a generalized fucntion which can take "close_price"
	"open_price", "quantity", "open-interest" as type values.
	By default type="close_price"
    dateformat: "YYYY-MM-DD"
    return: return list of values during from-to period
	"""
    secid=str(secId)
    cursor=db.ticker.find_one({"_id":secid})

    obj=cursor['ticker']
    hourArr=['091559','101559','111559','121559','131559','141559','151559']
    dFrom=dateutil.parser.parse(datefrom)
    dTo=dateutil.parser.parse(dateto)
    delta = datetime.timedelta(days=1)
    dateArr=[]
    while dFrom <= dTo:
        dateArr.append(str(dFrom.strftime("%d%m%Y")))
        dFrom += delta
    if dataType=='array':
        if frequency=='minute':
            arr=[]
            for key in dateArr:
                dateArr=[]
                try:
                    sortedKey=sorted(obj[key])
                    for timekey in sortedKey:
                        try:
                            dateArr.append(obj[key][timekey][objectType])
                        except Exception as e:
                            print 'error', str(e)
                except Exception as e:
                    print 'error', str(e)
                if len(dateArr):
                    arr.append(dateArr)
            return arr
        elif frequency=='daily':
            arr=[]
            for key in dateArr:
                try:
                    arr.append(obj[key]['152959'][objectType])
                except Exception as e:
                    print 'error', str(e)
            return arr
        elif frequency=='hourly':
            arr=[]
            for key in dateArr:
                timeArr=[]
                for hour in hourArr:
                    try:
                        timeArr.append(obj[key][hour][objectType])
                    except Exception as e:
                        print 'error', str(e)
                if len(timeArr):
                    arr.append(timeArr)
            return arr
    else:
        if frequency=='minute':
            newdict={}
            for key in dateArr:
                datedict={}
                try:
                    for timekey in obj[key]:
                        try:
                            datedict[timekey]=obj[key][timekey][objectType]
                        except Exception as e:
                            print 'error', str(e)
                except Exception as e:
                    print 'error', str(e)
                newdict[key]=datedict
            return newdict
        elif frequency=='daily':
            newdict={}
            for key in dateArr:
                try:
                    newdict[key]=obj[key]['152959'][objectType]
                except Exception as e:
                    print 'error', str(e)
            return newdict
        elif frequency=='hourly':
            overdict={}
            for key in dateArr:
                timedict={}
                for hour in hourArr:
                    try:
                        timedict[hour]=obj[key][hour][objectType]
                    except Exception as e:
                        print 'error', str(e)
                overdict[key]=timedict
            return overdict
# print fetch_secId('ACC','future',None,None,'current')
# print fetch_price('101','2014-09-03T12:15:59','minute') ---> 1479.3
# print fetch_data('101','2014-09-03T12:15:59','daily','closeValue') ---> 1467
# print fetch_price_list('101','2014-09-03','2014-12-04','minute') ---> [u'1727.45', u'1694.2', u'1667.4', u'1688.85', u'1688', u'1660'],[u'1667.4', u'1688.85', u'1688'],...]
# print fetch_data_list('101','2014-09-25','2014-09-26','hourly') ---> [[u'1727.45', u'1694.2', u'1667.4', u'1688.85', u'1688', u'1660'],[u'1667.4', u'1688.85', u'1688'],...]
# print("--- %s seconds ---" % (time.time() - start_time))
