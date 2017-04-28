from engine.drivers import feedapi

class StrategySimulator(object):
    def __init__(self, from_date, to_date, trade_frequency, shares, securityId, strategyCriterion):
        """
        input: from_date: 'YYYY-MM-DDTHH:MM',
               to_date: 'YYYY-MM-DDTHH:MM',
               trade_frequency: 'minute', 'hourly', 'daily', 'weekly', 'monthly',
               shares: <int>,
               securityId: <secId>,
               strategyCriterion: <StrategyCriterion class object>

        """
        pass

    def load_data(self, from_date, to_date, trade_frequency, securityId, objectType='close_price'):
        """
        Load prices/volume as per frequency, from_date, to_date and securityId using feedapi.
        Convert it to pandas.DataFrame for further process

        return Daraframe containing the data
        """
        return 1

    def simulate(self):
        """
        Simulate strategy from from_date to to_date
        returns Performance class object
        """
        return True

class StrategyCriterion(object):
    operators = ('>=', '<=', '==', '>', '<', '!=')
    brackets = ('(', ')')

    def __init__(self, enter_criterion=None, exit_criterion=None, stop_loss=None, profit_booking=None):
        """
        enter_criterion: <type str> 'ema(20) >= sma(10)'
        exit_criterion: <type str> 'ema(20) >= sma(10)'
        stop_loss: <type %>
        profit_booking: <type %>

        return a dict:
        {
            'stop_loss': <type %>,
            'profit_booking': <type %>,
            'enter_criterion': function,
            'exit_criterion': function
        }
        """
        pass

    def parse_criterion(criterion):


class Performance(object):
    def __init__(self):
        pass
