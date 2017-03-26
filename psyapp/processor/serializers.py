from rest_framework import serializers

from .models import Strategy, Ticker
from users.serializers import UserSerializer

class TickerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticker
        fields = ('symbol', 'exchange')

class StrategySerializer(serializers.ModelSerializer):
    ticker = TickerSerializer(many=False)

    class Meta:
        model = Strategy
        fields = ('pk', 'strategy', 'ticker', 'shares', 'is_active', 'name')
