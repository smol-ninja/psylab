from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response

from .serializers import StrategySerializer, TickerSerializer, IndicatorsSerializer
from .models import Strategy, Ticker, Indicators

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
    pass
