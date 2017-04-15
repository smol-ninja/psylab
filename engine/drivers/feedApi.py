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
        obj=cursor[dateValue][timeValue]
        return obj['closeValue']
    elif frequency=='daily':
        timeValue='152959'
        obj=cursor[dateValue][timeValue]
        return obj['closeValue']
    elif frequency=='hourly':
        timeValue=str(d.strftime('%H'))
        if timeValue[0]=='0':
            timeValue=timeValue[1:]
        timeValue=timeValue+'1559'
        obj=cursor[dateValue][timeValue]
        return obj['closeValue']
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
    obj=cursor[dateValue][timeValue]
    return obj[type]
