from django.conf.urls import include, url

from .views import strategy_view, ticker_view, indicator_view, backtest_view

urlpatterns = [
    url(r'^eng/$', strategy_view, name='strategy'),
    url(r'^eng/(?P<pk>[0-9]+)/$', strategy_view, name='strategy'),
    url(r'^tickers', ticker_view, name='ticker'),
    url(r'^indicators', indicator_view, name='indicators'),
    url(r'^backtest', backtest_view, name='backtests'),
]
