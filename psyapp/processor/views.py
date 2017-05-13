import time
import base64
import hashlib
import pytz
from datetime import datetime

from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response

from .serializers import StrategySerializer, TickerSerializer, IndicatorsSerializer
from .models import Strategy, Ticker, Indicators, Backtests
from slp import NLPService

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

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def indicator_view(request):
    if request.method == 'GET':
        indicators_list = Indicators.objects.all()
        il = IndicatorsSerializer(indicators_list, many=True)
        return Response(status=200, data=il.data)

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
        trade_frequency = request.data['frequency']
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
        return Response(status=200, data={'backtestId': buid})
