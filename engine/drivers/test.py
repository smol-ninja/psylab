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

print db.symbol_sid.find_one({ "_id": { '$exists': True } })
print db.psytest.find_one({ "_id": "5021712017120" })
