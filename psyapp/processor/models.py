from __future__ import unicode_literals
from django.db import models
from django.core.validators import RegexValidator

from users.models import User

# Create your models here.
DAY = 'daily'
WEEK = 'weekly'
MINUTE = 'minute'
HOUR = 'hourly'
MONTH = 'monthly'
TRADE_FREQUENCY_CHOICES = (
    (DAY, 'daily'),
    (WEEK, 'weekly'),
    (MINUTE, 'minute'),
    (HOUR, 'hourly'),
    (MONTH, 'monthly')
)

class Ticker(models.Model):
    NSE = 'nse'
    EXCHANGE_CHOICES = (
        (NSE, 'nse'),
    )
    symbol = models.CharField(max_length=20, primary_key=True)
    exchange = models.CharField(max_length=6, choices=EXCHANGE_CHOICES, default=NSE)
    uin = models.CharField(max_length=20, unique=True, blank=True)

    def __unicode__(self):
        return self.symbol

class Strategy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=30, blank=True, null=False)
    buy_strategy = models.CharField(max_length=999, blank=True, null=True)
    decoded_buy_strategy = models.CharField(max_length=999, blank=True, null=True)
    sell_strategy = models.CharField(max_length=999, blank=True, null=True)
    decoded_sell_strategy = models.CharField(max_length=999, blank=True, null=True)
    ticker = models.ForeignKey(Ticker, on_delete=models.CASCADE, null=True)
    trade_frequency = models.CharField(max_length=10, choices=TRADE_FREQUENCY_CHOICES, default=DAY)
    stop_loss = models.FloatField(null=True)
    profit_booking = models.FloatField(null=True)
    shares = models.PositiveIntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Strategies'

    def __unicode__(self):
        return self.name

class Indicators(models.Model):
    abbreviation = models.CharField(max_length=10, blank=True, null=False, unique=True)
    name = models.CharField(max_length=50, blank=True, null=False, unique=True)

    class Meta:
        verbose_name_plural = 'Indicators'

    def __unicode__(self):
        return self.name

class Backtests(models.Model):
    buid = models.CharField(max_length=32, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    strategy = models.ForeignKey(Strategy, null=True)
    ticker = models.ForeignKey(Ticker, on_delete=models.CASCADE, null=True)
    trade_frequency = models.CharField(max_length=10, choices=TRADE_FREQUENCY_CHOICES, default=DAY)
    trade_quantity = models.PositiveIntegerField(null=True, blank=True)
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)

    # Performance fields
    pnl = models.FloatField(null=True)
    volatility = models.FloatField(null=True)
    sharpe_ratio = models.FloatField(null=True)
    sortino_ratio = models.FloatField(null=True)
    max_drawdown = models.FloatField(null=True)
    winning_rate = models.FloatField(null=True)
    losing_rate = models.FloatField(null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name_plural = 'Backtests'

    def __unicode__(self):
        return self.buid
