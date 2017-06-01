import csv
import itertools
import calendar
import glob
from pymongo import MongoClient
from os.path import dirname, realpath
import uuid
import os
dir_path=dirname(realpath(__file__))
path=(dir_path+'/../../backdata/*.csv')

client = MongoClient()
db = client.tickdata



def insert_sid_data(sid=None,date=None,timeValue=None,openValue=None,highValue=None,lowValue=None,closeValue=None,volume=None,openInterest=None):
    """
    Usage: Inserting sid document in ticker collection
    """
    # print "inserting data"
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
    # print "inserting Datedata"
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
    # print "updating data"
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


def create_sid(ticker):
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
            if symbol[0] in ['BANKNIFTY','NIFTY']:
                sid=symbol[0]
            else:
                pass
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
    return sid

def csvs_to_csv():
    firstRun=True
    list_files=list(glob.glob(path))
    for m in range (0,len(list_files),10):
        fout=open("out.csv","a")
        for i in range(m,m+left):
            csvFile=open(list_files[i])
            for line in csvFile:
                fout.write(line)
            csvFile.close()
        fout.close()
        write_db(firstRun)
        os.remove("out.csv")
        firstRun=False
        print len(list_files)-(m+left)
        if len(list_files)-(m+left) < 10:
            left=len(list_files)-(m+left)
def is_date(dt,previous_dt):
    """
    Usage: Return boolean value after date comparison
    """
    if previous_dt is None or previous_dt!=dt:
        return True
    else:
        return False

def write_db(firstRun):
    csvFile = open("out.csv")
    csvReader = csv.reader(csvFile)
    data = list(csvReader)
    data=sorted(data, key=lambda x: x[0], reverse=False)
    lastData={"ticker":None, "sid": None, "date":None}
    for row in range(0,len(data)):
        try:
            symTyp=data[row][0].split('-')
        except Exception as e:
            pass
        if symTyp[len(symTyp)-1]=='I':
            # print data[row]
            try:
                ticker_col=["".join(x) for _, x in itertools.groupby(data[row][0], key=str.isdigit)]
                len_ticker=len(ticker_col)
                ticker_col[0:len_ticker]=[''.join(ticker_col[0:len_ticker])]
                current_date=(data[row][1].replace("/",""))
                current_time=(data[row][2].replace(":",""))
                if current_time[0]=='9':
                    current_time='0'+current_time
                # print data[row]
                openValue=data[row][3]
                highValue=data[row][4]
                lowValue=data[row][5]
                closeValue=data[row][6]
                volume=data[row][7]
                openInterest=data[row][8]
                if lastData['ticker'] is None:
                    sid=create_sid(ticker_col)
                    if firstRun:
                    # print sid,current_date,current_time,openValue,highValue,lowValue,closeValue,volume,openInterest
                        insert_sid_data(sid,current_date,current_time,openValue,highValue,lowValue,closeValue,volume,openInterest)
                    else:
                        insert_datetime_data(sid,current_date,current_time,openValue,highValue,lowValue,closeValue,volume,openInterest)
                    lastData['ticker']=ticker_col[0]
                    lastData['sid']=sid
                    lastData['date']=current_date
                elif ticker_col[0]==lastData['ticker']:
                    sid=lastData['sid']
                    if lastData['date']==current_date:
                        update_datetime_data(sid,current_date,current_time,openValue,highValue,lowValue,closeValue,volume,openInterest)
                    else:
                        insert_datetime_data(sid,current_date,current_time,openValue,highValue,lowValue,closeValue,volume,openInterest)
                        lastData['date']=current_date
                elif ticker_col[0]!=lastData['ticker']:
                    sid=create_sid(ticker_col)
                    if firstRun:
                    # print sid,current_date,current_time,openValue,highValue,lowValue,closeValue,volume,openInterest
                        insert_sid_data(sid,current_date,current_time,openValue,highValue,lowValue,closeValue,volume,openInterest)
                    else:
                        insert_datetime_data(sid,current_date,current_time,openValue,highValue,lowValue,closeValue,volume,openInterest)
                    # print sid,current_date,current_time,openValue,highValue,lowValue,closeValue,volume,openInterest
                    lastData['ticker']=ticker_col[0]
                    lastData['sid']=sid
                    # pass
            except Exception as e:
                pass

csvs_to_csv()
