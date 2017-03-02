import csv
import itertools
import calendar
import glob
from pymongo import MongoClient

client = MongoClient()
db = client.tickdata

if db.symbol_sid.find_one({ "_id": { '$exists': True } }) is None:
    db.sid_counter.insert({'_id': "sid", 'seq': 0})

def insert_sid_data(sid=None,date=None,timeValue=None,openValue=None,highValue=None,lowValue=None,closeValue=None,volume=None,openInterest=None):
    print "inserting data"
    db.ticker.insert_one({
        "_id":sid,
        "ticker":{
            date:{
                    timeValue:{
                    "openValue":openValue,
                   "highValue":highValue,
                   "lowValue":lowValue,
                   "closeValue":closeValue,
                   "volume":volume,
                   "openInterest":openInterest}

                }
        }
    })

def insert_datetime_data(sid=None,date=None,timeValue=None,openValue=None,highValue=None,lowValue=None,closeValue=None,volume=None,openInterest=None):
    print "inserting Datedata"
    update_field="ticker."+date
    db.ticker.update_one({
      "_id": sid
    },  {"$set": {update_field:{
                    timeValue:{
                    "openValue":openValue,
                   "highValue":highValue,
                   "lowValue":lowValue,
                   "closeValue":closeValue,
                   "volume":volume,
                   "openInterest":openInterest}
                    }
                }
    })

def update_datetime_data(sid=None,date=None,timeValue=None,openValue=None,highValue=None,lowValue=None,closeValue=None,volume=None,openInterest=None):
    print "updating data"
    update_field="ticker."+date+"."+timeValue
    db.ticker.update_one(
      {
        "_id":sid
      },
       { "$set": { update_field: {
                "openValue":openValue,
               "highValue":highValue,
               "lowValue":lowValue,
               "closeValue":closeValue,
               "volume":volume,
               "openInterest":openInterest
           }}}
      )

abbr_to_num = {name: num for num, name in enumerate(calendar.month_abbr) if num}

def is_date(dt,previous_dt):
    if previous_dt is None or previous_dt!=dt:
        return True
    else:
        return False

def get_next_sequence(collection,symbol):
   return collection.find_and_modify(query= { '_id': symbol },update= { '$inc': {'seq': 1}}, new=True ).get('seq')

def create_sid(ticker,fyear):
    if (db.symbol_sid.find_one({'symbol':ticker[0]})) is None:
        if "-" in ticker[0]:
            sid=get_next_sequence(db.sid_counter,"sid")
            if "III" in ticker[0]:
                expiry='three'
            elif "II" in ticker[0]:
                expiry='two'
            elif "I" in ticker[0]:
                expiry='one'
            else:
                expiry=None
            db.symbol_sid.insert({'sid': sid, 'symbol':ticker[0],'expiry':expiry,'option_type':'future'})
        else:
            sid=get_next_sequence(db.sid_counter,"sid")
            db.symbol_sid.insert({'sid': sid, 'symbol':ticker[0]})
    elif (db.symbol_sid.find_one({'symbol':ticker[0]})):
        result = db.symbol_sid.find_one({'symbol':ticker[0]})
        sid=result["sid"]
    if len(ticker)==5:
        print "option",
        sid='50'+str(sid)
        if ticker[4]=='PE':
            sid+='PE'
        else:
            sid+='CE'
        sid+=ticker[1]+(str(abbr_to_num[ticker[2].title()])+fyear+ticker[3])
    elif len(ticker)!=5 and ticker[0]!='Ticker':
        if "-" in ticker[0]:
            sid='10'+str(sid)
            print "future",
        else:
            sid='30'+str(sid)
            print "cash",
            sid+=ticker[1]+(str(abbr_to_num[ticker[2].title()]))+fileYear
    return sid

def write_mongo(data,row,ticker_col,fyear):
    sid=create_sid(ticker_col,fyear)
    previous_date=None
    current_date=(data[row][1].replace("/",""))
    current_time=(data[row][2].replace(":",""))
    print data[row]
    openValue=data[row][3]
    highValue=data[row][4]
    lowValue=data[row][5]
    closeValue=data[row][6]
    volume=data[row][7]
    openInterest=data[row][8]
    if 1<=row:
        previous_date=(data[row-1][1].replace("/",""))
        if db.ticker.find_one({ "_id":sid}):
            if is_date(current_date,previous_date):
                insert_datetime_data(sid,current_date,current_time,openValue,highValue,lowValue,closeValue,volume,openInterest)
            else:
                update_datetime_data(sid,current_date,current_time,openValue,highValue,lowValue,closeValue,volume,openInterest)
        elif db.ticker.find_one({ "_id":sid}) is None:
            insert_sid_data(sid,current_date,current_time,openValue,highValue,lowValue,closeValue,volume,openInterest)
    else:
        if db.ticker.find_one({ "_id":sid}):
            insert_datetime_data(sid,current_date,current_time,openValue,highValue,lowValue,closeValue,volume,openInterest)
        elif db.ticker.find_one({ "_id":sid}) is None:
            insert_sid_data(sid,current_date,current_time,openValue,highValue,lowValue,closeValue,volume,openInterest)


path=('/home/manish/Work/jan2016tofeb2017/*.csv')
for fname in glob.glob(path):
    print "file open", (fname)
    csvFile = open(fname)
    fyear=fname[-8:-4]
    csvReader = csv.reader(csvFile)
    data = list(csvReader)
    data=sorted(data, key=lambda x: x[0], reverse=False)
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
            write_mongo(data,row,ticker_col,fyear)
        else:
            ticker_col[0:len(ticker_col)]=[''.join(ticker_col[0:len(ticker_col)])]
            write_mongo(data,row,ticker_col,fyear)
    csvFile.close()
