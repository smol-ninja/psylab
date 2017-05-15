import csv
import itertools
import calendar
import glob
from pymongo import MongoClient

client = MongoClient()
db = client.tickdata
"""
Check if symbol_sid collection exists, if not then create
an autoincrement sid_counter collection
"""
csvFile = open('backdata/uin.csv')
csvReader = csv.reader(csvFile)
data = list(csvReader)
data=sorted(data, key=lambda x: x[0], reverse=False)
for row in range(0,len(data)):
    print data[row]
    db.uin.insert_one({
        "symbol":data[row][0],
        "sid":data[row][2]
    })
if db.symbol_sid.find_one({ "_id": { '$exists': True } }) is None:
    db.sid_counter.insert({'_id': "sid", 'seq': 0})

def insert_sid_data(sid=None,date=None,timeValue=None,openValue=None,highValue=None,lowValue=None,closeValue=None,volume=None,openInterest=None):
    """
    Usage: Inserting sid document in ticker collection
    """
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
    """
    Usage: Inserting datetime document or updating sid document in ticker collection
    """
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
    """
    Usage: Inserting time field or updating datetime document or
    updating sid document in ticker collection
    """
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

# convert abbreviations to number
abbr_to_num = {name: num for num, name in enumerate(calendar.month_abbr) if num}

def is_date(dt,previous_dt):
    """
    Usage: Return boolean value after date comparison
    """
    if previous_dt is None or previous_dt!=dt:
        return True
    else:
        return False

def get_next_sequence(collection,symbol):
    """
    Usage: Return integer value of elemets presents in symbol_sid collection
    using sid_counter
    """
    return collection.find_and_modify(query= { '_id': symbol },update= { '$inc': {'seq': 1}}, new=True ).get('seq')

def create_sid(ticker,fyear):
    """
    Usage: Create sid and return
    If Symbol not exists in symbol_sid collection
    Get count of symbols in symbol_sid collection
    using get_next_sequence
    Check option type and insert into symbol_sid collection
    """
    if db.symbol_sid.find_one({'symbol':ticker[0]}) is None:
        symbol=ticker[0].split('-')
        if len(symbol)>2:
            symbol[0]=symbol[0]+'-'+symbol[1]
        result=(db.uin.find_one({'symbol':symbol[0]}))
        try:
            sid=result['sid']
        except Exception as e:
            sid=symbol[0]
        if "III" in ticker[0]:
            expiry='three'
            sid=sid+'III'
        elif "II" in ticker[0]:
            expiry='next'
            sid=sid+'II'
        elif "I" in ticker[0]:
            expiry='current'
        else:
            expiry=None
        db.symbol_sid.insert({'sid': sid, 'symbol':ticker[0],'expiry':expiry,'securityType':'future'})
    elif (db.symbol_sid.find_one({'symbol':ticker[0]})):
        result = db.symbol_sid.find_one({'symbol':ticker[0]})
        sid=result["sid"]
    # if len(ticker)==5:
    #     sid='50'+str(sid)
    #     if ticker[4]=='PE':
    #         sid+='PE'
    #     else:
    #         sid+='CE'
    #     sid+=ticker[1]+(str(abbr_to_num[ticker[2].title()])+fyear+ticker[3])
    # elif len(ticker)!=5 and ticker[0]!='Ticker':
    #     if "-" in ticker[0]:
    #         sid='10'+str(sid)
    #         print "future",
    #     else:
    #         sid='30'+str(sid)
    #         print "cash",
    return sid

def write_mongo(data,row,ticker_col,fyear):
    """
    Usage: Write data in MongoDB
    Create SID using create_sid function
    """
    sid=create_sid(ticker_col,fyear)
    previous_date=None
    current_date=(data[row][1].replace("/",""))
    current_time=(data[row][2].replace(":",""))
    if current_time[0]=='9':
        current_time='0'+current_time
    # print data[row]
    try:
        symTyp=data[row][0].split('-')
    except Exception as e:
        pass
    if symTyp[len(symTyp)-1]=='I':
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
path=('backdata/*.csv')
for fname in glob.glob(path):
    """
    Sort data based on symbol
    Split ticker column based on integer and string type
    Check length of a ticker column array
    Normal check to reconstruct Symbol and valid strike price
    Call write_mongo function
    """
    print "file open", (fname)
    csvFile = open(fname)
    fyear=fname[-8:-4]
    csvReader = csv.reader(csvFile)
    data = list(csvReader)
    data=sorted(data, key=lambda x: x[0], reverse=False)
    for row in range(0,len(data)):
        # import pdb; pdb.set_trace()
        ticker_col=["".join(x) for _, x in itertools.groupby(data[row][0], key=str.isdigit)]
        len_ticker=len(ticker_col)

        if ticker_col[len_ticker-1]=='PE' or ticker_col[len_ticker-1]=='CE':
            # if 6<len_ticker:
            #     for i in range (0,len(ticker_col)):
            #         if ticker_col[i]=='.':
            #             ticker_col[i-1:i+2] = [''.join(ticker_col[i-1:i+2])]
            #             break
            #     if 6<=len(ticker_col):
            #         ticker_col[0:len(ticker_col)-4]=[''.join(ticker_col[0:len(ticker_col)-4])]
            # write_mongo(data,row,ticker_col,fyear)
            pass
        else:
            ticker_col[0:len(ticker_col)]=[''.join(ticker_col[0:len(ticker_col)])]
            write_mongo(data,row,ticker_col,fyear)
    csvFile.close()
