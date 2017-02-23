import csv
import itertools
import calendar
from itertools import groupby
from pymongo import MongoClient
from datetime import datetime
import string
import time
import datetime as dt
client = MongoClient()
db = client.test

if db.symbol_sid.find_one({ "_id": { '$exists': True } }) is None:
    db.sid_counter.insert({'_id': "sid", 'seq': 0})

def insertSid_data(sid=None,date=None,time=None,open=None,high=None,low=None,close=None,volume=None,open_interest=None):
    print "inserting data"
    result=db.psytest.insert_one({
        "_id":sid,
        "ticker":{
            date:{
                    time:{
                    "high":high,
                    "low":low,
                    "close":close,
                    "volume":volume,
                    "openInterest":open_interest}

                }
        }
    })

def insertDatetime_data(sid=None,date=None,time=None,open=None,high=None,low=None,close=None,volume=None,open_interest=None):
    print "inserting Datedata"
    update_field="ticker."+date
    db.psytest.update_one({
      "_id": sid
    },  {"$set": {update_field:{
                    time:{
                    "high":high,
                    "low":low,
                    "close":close,
                    "volume":volume,
                    "openInterest":open_interest}
                    }
                }
    })

def updateDatetime_data(sid=None,date=None,time=None,open=None,high=None,low=None,close=None,volume=None,open_interest=None):
    print "updating data"
    update_field="ticker."+date+"."+time
    db.psytest.update_one(
      {
        "_id":sid
      },
       { "$set": { update_field: {
               "high":high,
               "low":low,
               "close":close,
               "volume":volume,
               "openInterest":open_interest
           }}}
      )

abbr_to_num = {name: num for num, name in enumerate(calendar.month_abbr) if num}

def isDate(dt,previous_dt):
    if previous_dt is None or previous_dt!=dt:
        return True
    else:
        return False

def RepresentsInt(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def getNextSequence(collection,symbol):
   return collection.find_and_modify(query= { '_id': symbol },update= { '$inc': {'seq': 1}}, new=True ).get('seq')

def createSid(ticker):
    sid=None
    fileYear="2017"
    if (db.symbol_sid.find_one({'symbol':ticker[0]})) is None:
        if "-" in ticker[0]:
            sid=getNextSequence(db.sid_counter,"sid")
            if "III" in ticker[0]:
                expiry='three'
            elif "II" in ticker[0]:
                expiry='two'
            elif "I" in ticker[0]:
                expiry='one'
            db.symbol_sid.insert({'sid': sid, 'symbol':ticker[0],'expiry':expiry,'option_type':'future'})
        else:
            sid=getNextSequence(db.sid_counter,"sid")
            db.symbol_sid.insert({'sid': sid, 'symbol':ticker[0]})
    elif (db.symbol_sid.find_one({'symbol':ticker[0]})):
        result = db.symbol_sid.find_one({'symbol':ticker[0]})
        sid=result["sid"]
    if len(ticker)==5:
        print "option",
        sid='50'+str(sid)
        sid+=ticker[1]+(str(abbr_to_num[ticker[2].title()])+fileYear+ticker[3])
        if ticker[4]=='PE':
            sid+='1'
        else:
            sid+='0'
    elif len(ticker)!=5:
        if "-" in ticker[0]:
            sid='10'+str(sid)
            print "future",
        else:
            sid='30'+str(sid)
            print "cash",
            sid+=ticker[1]+(str(abbr_to_num[ticker[2].title()]))+fileYear
    return sid

def writeMongo(data,row,ticker_col):
    sid=createSid(ticker_col)
    previous_date=None
    current_date=(data[row][1].replace("/",""))
    current_time=(data[row][2].replace(":",""))
    print data[row]
    open=data[row][3]
    high=data[row][4]
    low=data[row][5]
    close=data[row][6]
    volume=data[row][7]
    open_interest=data[row][8]
    if 1<=row:
        if not firstRun:
            previous_date=(data[row-1][1].replace("/",""))
            previous_time=(data[row-1][2].replace(":",""))
        if db.psytest.find_one({ "_id":sid}):
            if isDate(current_date,previous_date):
                insertDatetime_data(sid,current_date,current_time,open,high,low,close,volume,open_interest)
            else:
                updateDatetime_data(sid,current_date,current_time,open,high,low,close,volume,open_interest)
        elif db.psytest.find_one({ "_id":sid}) is None:
            insertSid_data(sid,current_date,current_time,open,high,low,close,volume,open_interest)
    else:
        if db.psytest.find_one({ "_id":sid}):
            insertDatetime_data(sid,current_date,current_time,open,high,low,close,volume,open_interest)
        elif db.psytest.find_one({ "_id":sid}) is None:
            insertSid_data(sid,current_date,current_time,open,high,low,close,volume,open_interest)

csvFile = open('NSEF&O_09012017.csv')
csvReader = csv.reader(csvFile)
data = list(csvReader)
# sorting data by name
data=sorted(data, key=lambda x: x[0], reverse=False)
firstRun=True
for row in range(0,len(data)):
    ticker_col=["".join(x) for _, x in itertools.groupby(data[row][0], key=str.isdigit)]
    len_ticker=len(ticker_col)
    if ticker_col[len_ticker-1]=='PE' or ticker_col[len_ticker-1]=='CE':
        if 6<len_ticker:
            for i in range (0,len(ticker_col)):
                if ticker_col[i]=='.':
                    ticker_col[i-1:i+2] = [''.join(ticker_col[i-1:i+2])]
                    break
            if 6<=len(ticker_col):
                ticker_col[0:len(ticker_col)-4]=[''.join(ticker_col[0:len(ticker_col)-4])]
        writeMongo(data,row,ticker_col)
    else:
        ticker_col[0:len(ticker_col)]=[''.join(ticker_col[0:len(ticker_col)])]
        writeMongo(data,row,ticker_col)
    firstRun=False
