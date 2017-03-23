from django.contrib import admin

from .models import Ticker, Strategy

# Register your models here.
class StrategyAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'strategy', 'ticker', 'user', 'is_active', 'created')
    list_filter = ('is_active', 'ticker')

class TickerAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'exchange')
    list_filter = ('exchange', )

admin.site.register(Strategy, StrategyAdmin)
admin.site.register(Ticker, TickerAdmin)
