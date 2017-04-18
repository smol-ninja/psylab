from pymongo import MongoClient
import datetime, dateutil.parser

client = MongoClient()
db = client.tickdata
def fetch_price(secid, datetime, frequency):
    d = dateutil.parser.parse(datetime)
    secid=str(secid)
    dateValue=str(d.strftime('%d%m%Y'))
    cursor=db.ticker.find_one({"_id":secid})
    if frequency=='minute':
        timeValue=str(d.strftime('%H%M%S'))
        if timeValue[0]=='0':
            timeValue=timeValue[1:]
        try:
            obj=cursor['ticker'][dateValue][timeValue]
            return obj['closeValue']
        except Exception as e:
            print 'error', str(e)
    elif frequency=='daily':
        timeValue='152959'
        try:
            obj=cursor['ticker'][dateValue][timeValue]
            return obj['closeValue']
        except Exception as e:
            print 'error', str(e)
    elif frequency=='hourly':
        timeValue=str(d.strftime('%H'))
        if timeValue[0]=='0':
            timeValue=timeValue[1:]
        timeValue=timeValue+'1559'
        try:
            obj=cursor['ticker'][dateValue][timeValue]
            return obj['closeValue']
        except Exception as e:
            print 'error', str(e)
    # TODO: weekly condition
    # else:
    #     day=d.strptime(dateValue, '%d%m%Y').strftime('%A')
def fetch_data(secid, datetime, type="closeValue"):
    d=dateutil.parser.parse(datetime)
    secid=str(secid)
    dateValue=str(d.strftime('%d%m%Y'))
    cursor=db.ticker.find_one({"_id":secid})
    timeValue=str(d.strftime('%H%M%S'))
    if timeValue[0]=='0':
        timeValue=timeValue[1:]
    try:
        obj=cursor['ticker'][dateValue][timeValue]
        return obj[type]
    except Exception as e:
        print 'error', str(e)
def fetch_price_list(secId, datefrom, dateto, frequency):
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
        try:
            newdict = {key:obj[key] for key in dateArr}
            return newdict
        except Exception as e:
            print 'error', str(e)
    elif frequency=='daily':
        try:
            newdict = {key:obj[key]['153059'] for key in dateArr}
            return newdict
        except Exception as e:
            print 'error', str(e)
    elif frequency=='hourly':
        overdict={}
        for key in dateArr:
            timedict={}
            for hour in hourArr:
                try:
                    timedict[hour]=obj[key][hour]
                except Exception as e:
                    print 'error', str(e)
            overdict[key]=timedict
        return overdict
    # TODO: weekly
print fetch_price_list('101','2017-01-09','2017-01-09','hourly')
