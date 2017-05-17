from django.contrib import admin
from django.conf import settings
from django.http import HttpResponseRedirect
from django.conf.urls import include, url
from django.contrib.admin.views.decorators import staff_member_required

from .models import Ticker, Strategy, Indicators, Backtests

# View to update symbols
@staff_member_required
def update_symbols(request):
    with open(settings.BASE_DIR+'/data/equity.csv', 'r') as f:
        lines = f.readlines()
        for line in lines:
            tokens = line.split(',')
            if tokens[2] == 'EQ':
                Ticker.objects.update_or_create(symbol=tokens[0], uin=tokens[6])
    f.close()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])

# Register your models here.
class StrategyAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'buy_strategy', 'decoded_buy_strategy', 'sell_strategy', 'decoded_sell_strategy', 'ticker', 'shares', 'trade_frequency', 'stop_loss', 'profit_booking', 'user', 'is_active', 'updated')
    list_filter = ('is_active', 'trade_frequency')
    search_fields = ['ticker__symbol']

class TickerAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'uin', 'exchange')
    list_filter = ('exchange', )
    search_fields = ['symbol']

    def get_urls(self):
        urls = super(TickerAdmin, self).get_urls()
        update_urls = [
            url(r'^update/$', update_symbols)
        ]
        return update_urls + urls

class IndicatorsAdmin(admin.ModelAdmin):
    list_display = ('abbreviation', 'name')
    search_fields = ['abbreviation']

class BacktestsAdmin(admin.ModelAdmin):
    list_display = ('buid', 'strategy_id', 'ticker', 'trade_frequency', 'trade_quantity', 'pnl', 'volatility', 'sharpe_ratio', 'sortino_ratio', 'max_drawdown', 'winning_rate', 'losing_rate', 'start', 'user', 'end', 'created')

admin.site.register(Strategy, StrategyAdmin)
admin.site.register(Ticker, TickerAdmin)
admin.site.register(Indicators, IndicatorsAdmin)
admin.site.register(Backtests, BacktestsAdmin)
