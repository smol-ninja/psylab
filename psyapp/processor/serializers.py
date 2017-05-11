from rest_framework import serializers

from .models import Strategy, Ticker, Indicators, Backtests
from users.serializers import UserSerializer

class TickerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticker
        fields = ('symbol', 'exchange')

class StrategySerializer(serializers.ModelSerializer):
    ticker = TickerSerializer(many=False)

    class Meta:
        model = Strategy
        fields = ('pk', 'strategy', 'ticker', 'shares', 'trade_frequency', 'stop_loss', 'profit_booking', 'is_active', 'name', 'updated')

class IndicatorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicators
        fields = ('abbreviation', 'name')

class BacktestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Backtests
        fields = ('buid', 'strategy_id', 'ticker', 'trade_frequency', 'trade_quantity', 'pnl', 'volatility', 'sharpe_ratio', 'sortino_ratio', 'max_drawdown', 'winning_rate', 'losing_rate', 'start', 'end')
