import time
import base64
import hashlib
import pytz
from datetime import datetime
from dateutil import parser

import pandas as pd
import random
from random import randint
import numpy as np

from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response

from .serializers import StrategySerializer, TickerSerializer, IndicatorsSerializer
from .models import Strategy, Ticker, Indicators, Backtests
from slp import NLPService
from .dataset import Dataset
from .simulator import StrategyPerformance
# from .simulator import StrategyCriterion, StrategPerformance, StrategySimulator

# Create your views here.l
@api_view(['POST', 'GET', 'PUT', 'DELETE'])
@login_required()
def strategy_view(request, **kwargs):
    """
    Saving Strategies
    """
    if request.method == 'POST':
        try:
            ticker = Ticker.objects.get(symbol=request.data['ticker'])
        except Exception as e:
            return Response(status=404, data={'error': e.message})
        if Strategy.objects.filter(name=request.data['name'], user=request.user):
            return Response(status=400, data={'error': 'Strategy name: %s already exists. Choose a different name.' % (request.data['name'])})
        strategy = Strategy.objects.create(
                name=request.data['name'],
                user=request.user,
                strategy=request.data['strategy'],
                ticker=ticker,
                shares=request.data['shares'],
                stop_loss=request.data['stop_loss'],
                profit_booking=request.data['profit_booking'],
                trade_frequency=request.data['trade_frequency']
            )
        strategySerializer = StrategySerializer(instance=strategy)
        return Response(status=200, data=strategySerializer.data)

    elif request.method == 'GET':
        strategies = Strategy.objects.filter(user=request.user)
        strategiesSerializer = StrategySerializer(strategies, many=True)
        return Response(status=200, data=strategiesSerializer.data)

    elif request.method == 'PUT':
        try:
            Strategy.objects.filter(pk=kwargs['pk'], user=request.user).update(**request.data)
            return Response(status=200)
        except Exception as e:
            return Response(status=404, data={'error': e.message})

    elif request.method == 'DELETE':
        try:
            instance = Strategy.objects.get(pk=kwargs['pk'], user=request.user)
            instance.delete()
            return Response(status=200)
        except Exception as e:
            return Response(status=404, data={'error': e.message})

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def ticker_view(request):
    if request.method == 'GET':
        ticker_lists = Ticker.objects.all()
        ts = TickerSerializer(ticker_lists, many=True)
        return Response(status=200, data=ts.data)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def fetch_sid_view(request):
    """
    It will return sid corresponding to symbol.
    Url: /api/sid
    """
    if request.method == 'POST':
        try:
            ticker = Ticker.objects.get(symbol=request.data['symbol'])
            ticker=TickerSerializer(ticker, many=False)
            return Response(status=200, data=ticker.data)
        except Exception as e:
            return Response(status=404, data={'error': e.message})

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def indicator_view(request):
    if request.method == 'GET':
        indicators_list = Indicators.objects.all()
        il = IndicatorsSerializer(indicators_list, many=True)
        return Response(status=200, data=il.data)

def dummy_dataframe(start, end):
    """
    Input: Nothing, this function will create a dummy dataframe of orders of size 10
    return:
                sid  share side  price  re  unre  openposition  avgPrice
    2017-05-07    1      2    B     23   0   0.0             2      23.0
    2017-05-08    1      2    S     30  14   0.0             0       0.0
    2017-05-09    1      2    B     29  14   0.0             2      29.0
    2017-05-10    1      2    B     66  14  74.0             4      47.5
    2017-05-11    1      2    S     27 -27   0.0             2      47.5
    2017-05-12    1      2    S     54 -14   0.0             0       0.0
    2017-05-13    1      2    B     48 -14   0.0             2      48.0
    2017-05-14    1      2    S     30 -50   0.0             0       0.0
    2017-05-15    1      2    S     63 -50   0.0            -2      63.0
    2017-05-16    1      2    S     56 -50  14.0            -4      59.5
    """
    start=start.strftime("%Y-%m-%d")
    end=end.strftime("%Y-%m-%d")
    start = datetime.strptime(start, "%Y-%m-%d").date()
    end = datetime.strptime(end, "%Y-%m-%d").date()
    print start, end
    index = pd.date_range(start, periods=((end-start).days)+1, freq='D')
    columns = ['sid','share', 'side','price','re','unre', 'openposition','avgPrice']
    df= pd.DataFrame(index=index, columns=columns)
    df['sid']=1
    df['share']=randint(1,10)
    df['side']=df['side'].apply(lambda v: random.choice(['B','S']))
    df['price']=df['price'].apply(lambda v: randint(20,100))
    df['openposition']=0
    df['unre']=0.0
    df['avgPrice']=0.0
    for i in range (0,len(df.index)):
        if i==0:
            df.loc[:,'re']=0
            if df['side'][0]=='B':
                df['openposition'][0]=df['share'][0]
                df['avgPrice'][0]=float(df['price'][0])
            elif df['side'][0]=='S':
                df['openposition'][0]=-df['share'][0]
                df['avgPrice'][0]=float(df['price'][0])
        else:
            # import pdb; pdb.set_trace()
            if df['side'][i]=='B':
                df['openposition'][i]=df['openposition'][i-1]+df['share'][i]
                if df['openposition'][i]>0:
                    df['avgPrice'][i]=(df['avgPrice'][i-1]*df['openposition'][i-1]+df['share'][i]*df['price'][i])/df['openposition'][i]
                elif df['openposition'][i]==0:
                    df['avgPrice'][i]=0
                else:
                    df['avgPrice'][i]=df['avgPrice'][i-1]
            if df['side'][i]=='S':
                df['openposition'][i]=df['openposition'][i-1]-df['share'][i]
                if df['openposition'][i]<0:
                    df['avgPrice'][i]=(abs(df['avgPrice'][i-1]*df['openposition'][i-1])+df['share'][i]*df['price'][i])/abs(df['openposition'][i])
                elif df['openposition'][i]==0:
                    df['avgPrice'][i]=0
                else:
                    df['avgPrice'][i]=df['avgPrice'][i-1]
            if abs(df['openposition'][i-1])-abs(df['openposition'][i])>0:
                if df['openposition'][i-1]>0:
                    df['re'][i]=((df['price'][i]-df['avgPrice'][i-1])*(df['share'][i]))+df['re'][i-1]
                elif df['openposition'][i-1]<0:
                    df['re'][i]=((df['avgPrice'][i-1]-df['price'][i])*(df['share'][i]))+df['re'][i-1]
                else:
                    df['re'][i]=df['re'][i-1]
            if abs(df['openposition'][i-1])-abs(df['openposition'][i])<0:
                if df['openposition'][i-1]>0:
                    df['unre'][i]=(df['price'][i]-df['avgPrice'][i-1])*(df['share'][i])
                    df['re'][i]=df['re'][i-1]
                elif df['openposition'][i-1]<0:
                    df['unre'][i]=(df['avgPrice'][i-1]-df['price'][i])*(df['share'][i])
                    df['re'][i]=df['re'][i-1]
                else:
                    df['re'][i]=df['re'][i-1]
    return df

@api_view(['POST'])
@login_required
def backtest_view(request):
    if request.method == 'POST':
        """
        {
    	"strategy_id": 44,
    	"ticker": "INSECTICID",
    	"quantity": 1,
    	"frequency": "daily",
    	"start_time": "2017-02-03",
    	"end_time": "2017-02-05"
        }
        frequency in (minute, daily, hourly, weekly)
        start_time, end_time format: YYYY-MM-DD
        """
        user = request.user
        ticker = Ticker.objects.get(symbol=request.data['ticker'])
        strategy_id = request.data['strategy_id']
        strategy = Strategy.objects.get(user=request.user, pk=strategy_id)
        trade_quantity = int(request.data['quantity'])
        trade_frequency = request.data['frequency'].lower()
        start = request.data['start_time']
        end = request.data['end_time']
        start_year, start_month, start_date = [int(i) for i in start.split('-')]
        end_year, end_month, end_date = [int(i) for i in end.split('-')]
        if start > end:
            return Response(status=405, data={'error': 'start date cannot be greater than end data.'})
        else:
            start = pytz.timezone('Asia/Kolkata').localize(
                    datetime(
                        year=start_year,
                        month=start_month,
                        day=start_date,
                        hour=9,
                        minute=15,
            ))
            end = pytz.timezone('Asia/Kolkata').localize(
                    datetime(
                        year=end_year,
                        month=end_month,
                        day=end_date,
                        hour=15,
                        minute=30,
            ))

        # Creating backtest Unique ID
        epoch = str(int(time.time()))
        nonce = epoch + str(strategy_id)
        buid = base64.urlsafe_b64encode(hashlib.md5(nonce).digest())

        bo = Backtests.objects.create(
                buid=buid,
                user=user,
                strategy=strategy,
                ticker=ticker,
                trade_frequency=trade_frequency,
                trade_quantity=trade_quantity,
                start=start,
                end=end
        )

        # dataset = Dataset(secId=ticker.uin, from_date=start.strftime('%Y-%m-%d'), to_date=end.strftime('%Y-%m-%d'), frequency=trade_frequency)
        # strategy_criterion = StrategyCriterion(enter_criterion=strategy.decoded_buy_strategy, exit_criterion=strategy.decoded_sell_strategy, profit_booking=strategy.profit_booking, stop_loss=strategy.stop_loss)
        stats={}
        df=dummy_dataframe(start, end)
        sp=StrategyPerformance(df)
        stats={'anualized_return':round(sp.annualized_return(), 3),
               'anualized_standard':round(sp.annualized_std(), 3),
               'anualized_downside_standard':round(sp.annualized_downside_std(), 3),
               'anual_volume':round(sp.annual_vol(), 3),
               'sharpe_ratio':round(sp.sharpe_ratio(), 3),
               'sortino_ratio':round(sp.sortino_ratio(), 3),
               'max_drawdown':round(sp.max_drawdown(), 3),
               'realized_profit':df['re'],
               'unrealized_profit':df['unre'],
               'order_history':df['openposition'],
               'backtestId': buid
               }
        # import pdb; pdb.set_trace()
        # return Response(status=200, data={'backtestId': buid})
        return Response(status=200, data=stats)
