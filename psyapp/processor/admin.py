from django.contrib import admin
from django.conf import settings
from django.http import HttpResponseRedirect
from django.conf.urls import include, url
from django.contrib.admin.views.decorators import staff_member_required

from .models import Ticker, Strategy, Indicators

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
    list_display = ('pk', 'name', 'strategy', 'ticker', 'shares', 'user', 'is_active', 'created')
    list_filter = ('is_active', )
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

admin.site.register(Strategy, StrategyAdmin)
admin.site.register(Ticker, TickerAdmin)
admin.site.register(Indicators, IndicatorsAdmin)
