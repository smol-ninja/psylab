from pymongo import MongoClient
import datetime, dateutil.parser

# import time
# start_time = time.time()
client = MongoClient()
db = client.tickdata
def fetch_price(secid, datetime, frequency):
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
    d=dateutil.parser.parse(datetime)
    if frequency=='minute':
        return fetch_data(secid,datetime,"closeValue")
    elif frequency=='daily':
        timeValue=d.replace(hour=15, minute=29,second=59).strftime('%Y-%m-%dT%H:%M:%S')
        return fetch_data(secid,timeValue,"closeValue")
    elif frequency=='hourly':
        timeValue=d.replace(minute=15,second=59).strftime('%Y-%m-%dT%H:%M:%S')
        return fetch_data(secid,timeValue,"closeValue")


    # TODO: weekly condition
    # else:
    #     day=d.strptime(dateValue, '%d%m%Y').strftime('%A')
def fetch_data(secid, datetime, objectType="closeValue"):
    """
	a generalized fucntion which can take "close_price"
	"open_price", "quantity", "open-interest" as type values.
	By default type="close_price"
    dateformat: "YYYY-MM-DDTHH:MM:SS"
    """
    d=dateutil.parser.parse(datetime)
    secid=str(secid)
    dateValue=str(d.strftime('%d%m%Y'))
    cursor=db.ticker.find_one({"_id":secid})
    timeValue=str(d.strftime('%H%M%S'))
    if timeValue[0]=='0':
        timeValue=timeValue[1:]
    try:
        obj=cursor['ticker'][dateValue][timeValue]
        return obj[objectType]
    except Exception as e:
        print 'error', str(e)
def fetch_price_list(secId, datefrom, dateto, frequency):
    return fetch_data_list(secId, datefrom, dateto, frequency,'closeValue')

def fetch_data_list(secId, datefrom, dateto, frequency,objectType="closeValue"):
    secid=str(secId)
    cursor=db.ticker.find_one({"_id":secid})
    obj=cursor['ticker']
    hourArr=['91559','101559','111559','121559','131559','141559','151559']
    dFrom=dateutil.parser.parse(datefrom)
    dTo=dateutil.parser.parse(dateto)
    delta = datetime.timedelta(days=1)
    dateArr=[]
    while dFrom <= dTo:
        dateArr.append(str(dFrom.strftime("%d%m%Y")))
        dFrom += delta
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
print fetch_price_list('101','2014-09-03','2014-12-04','minute')
# print("--- %s seconds ---" % (time.time() - start_time))
