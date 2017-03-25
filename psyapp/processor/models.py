from __future__ import unicode_literals
from django.db import models

from users.models import User

# Create your models here.
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
    strategy = models.CharField(max_length=999, blank=True, null=True)
    ticker = models.ForeignKey(Ticker, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Strategies'

class Indicators(models.Model):
    abbreviation = models.CharField(max_length=10, blank=True, null=False, unique=True)
    name = models.CharField(max_length=50, blank=True, null=False, unique=True)

    class Meta:
        verbose_name_plural = 'Indicators'

    def __unicode__(self):
        return self.abbreviation
