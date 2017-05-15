import csv
import itertools
import calendar
import glob
from pymongo import MongoClient

client = MongoClient()
db = client.tickdata
csvFile = open('uin.csv')
csvReader = csv.reader(csvFile)
data = list(csvReader)
data=sorted(data, key=lambda x: x[0], reverse=False)
# hy=(db.uin.find_one({'symbol':'ACE'}))
# print hy['uin']
for row in range(0,len(data)):
    print data[row]
    db.uin.insert_one({
        "symbol":data[row][0],
        "uin":data[row][2]
    })
# path=('backdata/*.csv')
# for fname in glob.glob(path):
#     """
#     Sort data based on symbol
#     Split ticker column based on integer and string type
#     Check length of a ticker column array
#     Normal check to reconstruct Symbol and valid strike price
#     Call write_mongo function
#     """
#     print "file open", (fname)
#     csvFile = open(fname)
#     fyear=fname[-8:-4]
#     csvReader = csv.reader(csvFile)
#     data = list(csvReader)
#     data=sorted(data, key=lambda x: x[0], reverse=False)
#     for row in range(0,len(data)):
#         print row
#         # import pdb; pdb.set_trace()
#         # ticker_col=["".join(x) for _, x in itertools.groupby(data[row][0], key=str.isdigit)]
#         # len_ticker=len(ticker_col)
#         # ticker_col[0:len(ticker_col)]=[''.join(ticker_col[0:len(ticker_col)])]
#         # write_mongo(data,row,ticker_col,fyear)
#     csvFile.close()
