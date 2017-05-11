import time
import base64
import hashlib

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
                decoded_strategy=NLPService(request.data['strategy']),
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
        request fields: {user: , strategy_id: , ticker: , quantity: , frequency: , start_time: , end_time: }.
        frequency in (minute, daily, hourly, weekly)
        start_time, end_time format: YYYY-MM-DD
        """
        user = request.user
        ticker = Ticker.objects.filter(symbol=request.data['ticker'])
        strategy_id = request['strategy_id']
        strategy = Strategy.objects.get(user=request.user, pk=strategy_id)
        trade_quantity = int(quantity)
        trade_frequency = request['frequency']
        start = request['start_time']
        end = request['end_time']

        # Creating backtest Unique ID
        epoch = str(int(time.time()))
        nonce = epoch + strategy_id
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
