from datetime import datetime
import sys
import os

masterSquareOffTime = (14, 00)
tpoints = (9, 20, 15, 20, 25)

def trading_begins():
    return (datetime.today().hour==tpoints[0] and datetime.today().minute==tpoints[1])
def trading_hours():
    return (datetime.today().hour==tpoints[0] and datetime.today().minute>tpoints[1]) or (datetime.today().hour==tpoints[2] and datetime.today().minute<tpoints[3]) or (datetime.today().hour>tpoints[0] and datetime.today().hour<tpoints[2])
def trading_ends():
    return (datetime.today().hour==tpoints[2] and datetime.today().minute>=tpoints[3])
def bidding_ends():
    return (datetime.today().hour==tpoints[2] and datetime.today().minute>=tpoints[4])

HOME_FOLDER_PATH = '/home/symphony'
# check if backup and report folder exist
if not os.path.exists(HOME_FOLDER_PATH + '/reports'):
    os.mkdir(HOME_FOLDER_PATH + '/reports')
if not os.path.exists(HOME_FOLDER_PATH + '/backup'):
    os.mkdir(HOME_FOLDER_PATH + '/backup')

class DevelopmentSettings(object):
    """Development Settings"""
    _URL = 'http://103.69.169.10:5602/gateway?wsdl'
    _ACCOUNT_ID = 'SS88'
    _USERNAME = 'shubham'
    _PASSWORD = 'sb@12345'
    _DATABASE = 'securities'
    _FEED_USERNAME = 'aa'
    _FEED_PASSWORD = 'aa'
    _MULTICAST_GROUP = "229.9.9.1"
    _MULTICAST_PORT = 9991
    _LOCALBIND_IP = "192.168.10.10"
    _ICHANNEL_PORT = 7777
    _LOCAL_UDP_PORT = 7000
    _ER_IP = '103.69.169.10'
    _ER_PORT = 5601

class PaperTradingSettings(object):
    """Paper Trading Settings"""
    _URL = 'http://192.168.45.16:9113/gateway?wsdl'
    _ACCOUNT_ID = 'SY8420'
    _USERNAME = 'shubham2'
    _PASSWORD = 'sy@12345'
    _DATABASE = 'securities'
    _FEED_USERNAME = 'aa'
    _FEED_PASSWORD = 'aa'
    _MULTICAST_GROUP = "227.9.9.9"
    _MULTICAST_PORT = 9991
    _LOCALBIND_IP = ''
    _ICHANNEL_PORT = 7777
    _LOCAL_UDP_PORT = 7000
    _ER_IP = '192.168.45.16'
    _ER_PORT = 9043

class LiveTradingSettings(object):
    """Live Trading Settings"""
    _URL = 'http://124.153.80.37:9103/gateway?wsdl'
    _ACCOUNT_ID = 'SAGAR315'
    _USERNAME = 'SAGARWAL'
    _PASSWORD = 'sg@45678'
    _DATABASE = 'live'
    _FEED_USERNAME = 'aa'
    _FEED_PASSWORD = 'aa'
    _MULTICAST_GROUP = "227.9.9.9"
    _MULTICAST_PORT = 9991
    _LOCALBIND_IP = ''
    _ICHANNEL_PORT = 7777
    _LOCAL_UDP_PORT = 7000
    _ER_IP = '124.153.80.37'
    _ER_PORT = 9033

class DatabaseConfig(object):
    USERNAME = 'shubham'
    PASSWORD = 'password'
    HOST = '127.0.0.1'

class FeedServerEnums(object):
    LOCALHOST = ''
    PORTS = [7100, 7200, 7300, 7400, 7500, 7600, 7700, 7800, 7900, 8000]
    NLOGS = 10

if len(sys.argv) != 2:
    sys.exit("Please provide an argument. If you don't know what I am talking about, please contact the owner.")

def get_url():
    if sys.argv[1] == 'dev':
        return DevelopmentSettings._URL
    elif sys.argv[1] == 'paper':
        return PaperTradingSettings._URL
    elif sys.argv[1] == 'live':
        return LiveTradingSettings._URL
    else:
        sys.exit("Invalid Argument. Available options are 1. dev 2. paper 3. live")

def get_table_to_export():
    if sys.argv[1] == 'dev':
        return ('securities', 'dev')
    elif sys.argv[1] == 'paper':
        return ('securities', 'paper')
    elif sys.argv[1] == 'live':
        return ('live', 'live')
    else:
        sys.exit("Invalid Argument. Available options are 1. dev 2. paper 3. live")

def get_account_id():
    if sys.argv[1] == 'dev':
        return DevelopmentSettings._ACCOUNT_ID
    elif sys.argv[1] == 'paper':
        return PaperTradingSettings._ACCOUNT_ID
    elif sys.argv[1] == 'live':
        return LiveTradingSettings._ACCOUNT_ID
    else:
        sys.exit("Invalid Argument. Available options are 1. dev 2. paper 3. live")

def get_username():
    if sys.argv[1] == 'dev':
        return DevelopmentSettings._USERNAME
    elif sys.argv[1] == 'paper':
        return PaperTradingSettings._USERNAME
    elif sys.argv[1] == 'live':
        return LiveTradingSettings._USERNAME
    else:
        sys.exit("Invalid Argument. Available options are 1. dev 2. paper 3. live")

def get_password():
    if sys.argv[1] == 'dev':
        return DevelopmentSettings._PASSWORD
    elif sys.argv[1] == 'paper':
        return PaperTradingSettings._PASSWORD
    elif sys.argv[1] == 'live':
        return LiveTradingSettings._PASSWORD
    else:
        sys.exit("Invalid Argument. Available options are 1. dev 2. paper 3. live")

def get_feedusername():
    if sys.argv[1] == 'dev':
        return DevelopmentSettings._FEED_USERNAME
    elif sys.argv[1] == 'paper':
        return PaperTradingSettings._FEED_USERNAME
    elif sys.argv[1] == 'live':
        return LiveTradingSettings._FEED_USERNAME
    else:
        sys.exit("Invalid Argument. Available options are 1. dev 2. paper 3. live")

def get_feedpassword():
    if sys.argv[1] == 'dev':
        return DevelopmentSettings._FEED_PASSWORD
    elif sys.argv[1] == 'paper':
        return PaperTradingSettings._FEED_PASSWORD
    elif sys.argv[1] == 'live':
        return LiveTradingSettings._FEED_PASSWORD
    else:
        sys.exit("Invalid Argument. Available options are 1. dev 2. paper 3. live")

def get_mcast_group():
    if sys.argv[1] == 'dev':
        return DevelopmentSettings._MULTICAST_GROUP
    elif sys.argv[1] == 'paper':
        return PaperTradingSettings._MULTICAST_GROUP
    elif sys.argv[1] == 'live':
        return LiveTradingSettings._MULTICAST_GROUP
    else:
        sys.exit("Invalid Argument. Available options are 1. dev 2. paper 3. live")

def get_mcast_port():
    if sys.argv[1] == 'dev':
        return DevelopmentSettings._MULTICAST_PORT
    elif sys.argv[1] == 'paper':
        return PaperTradingSettings._MULTICAST_PORT
    elif sys.argv[1] == 'live':
        return LiveTradingSettings._MULTICAST_PORT
    else:
        sys.exit("Invalid Argument. Available options are 1. dev 2. paper 3. live")

def get_localIp():
    if sys.argv[1] == 'dev':
        return DevelopmentSettings._LOCALBIND_IP
    elif sys.argv[1] == 'paper':
        return PaperTradingSettings._LOCALBIND_IP
    elif sys.argv[1] == 'live':
        return LiveTradingSettings._LOCALBIND_IP
    else:
        sys.exit("Invalid Argument. Available options are 1. dev 2. paper 3. live")

def get_ichannel_port():
    if sys.argv[1] == 'dev':
        return DevelopmentSettings._ICHANNEL_PORT
    elif sys.argv[1] == 'paper':
        return PaperTradingSettings._ICHANNEL_PORT
    elif sys.argv[1] == 'live':
        return LiveTradingSettings._ICHANNEL_PORT
    else:
        sys.exit("Invalid Argument. Available options are 1. dev 2. paper 3. live")

def get_udp_port():
    if sys.argv[1] == 'dev':
        return DevelopmentSettings._LOCAL_UDP_PORT
    elif sys.argv[1] == 'paper':
        return PaperTradingSettings._LOCAL_UDP_PORT
    elif sys.argv[1] == 'live':
        return LiveTradingSettings._LOCAL_UDP_PORT
    else:
        sys.exit("Invalid Argument. Available options are 1. dev 2. paper 3. live")

def get_er_ip():
    if sys.argv[1] == 'dev':
        return DevelopmentSettings._ER_IP
    elif sys.argv[1] == 'paper':
        return PaperTradingSettings._ER_IP
    elif sys.argv[1] == 'live':
        return LiveTradingSettings._ER_IP
    else:
        sys.exit("Invalid Argument. Available options are 1. dev 2. paper 3. live")

def get_er_port():
    if sys.argv[1] == 'dev':
        return DevelopmentSettings._ER_PORT
    elif sys.argv[1] == 'paper':
        return PaperTradingSettings._ER_PORT
    elif sys.argv[1] == 'live':
        return LiveTradingSettings._ER_PORT
    else:
        sys.exit("Invalid Argument. Available options are 1. dev 2. paper 3. live")

def get_database():
    if sys.argv[1] == 'dev':
        return DevelopmentSettings._DATABASE
    elif sys.argv[1] == 'paper':
        return PaperTradingSettings._DATABASE
    elif sys.argv[1] == 'live':
        return LiveTradingSettings._DATABASE
    else:
        sys.exit("Invalid Argument. Available options are 1. dev 2. paper 3. live")
