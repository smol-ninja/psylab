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
        obj=cursor['ticker'][dateValue][timeValue]
        return obj['closeValue']
    elif frequency=='daily':
        timeValue='152959'
        obj=cursor['ticker'][dateValue][timeValue]
        return obj['closeValue']
    elif frequency=='hourly':
        timeValue=str(d.strftime('%H'))
        if timeValue[0]=='0':
            timeValue=timeValue[1:]
        timeValue=timeValue+'1559'
        obj=cursor['ticker'][dateValue][timeValue]
        return obj['closeValue']
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
    obj=cursor['ticker'][dateValue][timeValue]
    return obj[type]
def fetch_price_list(secId, datefrom, dateto, frequency):
    secid=str(secId)
    cursor=db.ticker.find_one({"_id":secid})
    obj=cursor['ticker']
    dFrom=dateutil.parser.parse(datefrom)
    dTo=dateutil.parser.parse(dateto)
    d = dFrom
    delta = datetime.timedelta(days=1)
    dateArr=[]
    while d <= dTo:
        dateArr.append(str(d.strftime("%d%m%Y")))
        d += delta
    if frequency=='minute':
        newdict = {key:obj[key] for key in dateArr}
        return newdict
    elif frequency=="daily":
        newdict = {key:obj[key]['153059'] for key in dateArr}
        return newdict
    
vakue=fetch_price_list('101','2017-01-09','2017-01-09','minute')
for key, value in vakue.iteritems():
    print key, value
