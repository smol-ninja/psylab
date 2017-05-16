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
    gates = ('and', 'or')

    def __init__(self, enter_criterion=None, exit_criterion=None, stop_loss=None, profit_booking=None):
        """
        buy_criterion: <type str> 'ema(20) >= sma(10) and/or ema(20) >= sma(10)'
        sell_criterion: <type str> 'ema(20) >= sma(10) and/or ema(20) >= sma(10)'
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
        self.criterion_dict = {}
        try:
            stop_loss = float(stop_loss)
            if 0 <= stop_loss <= 100:
                self.criterion_dict.update({'stop_loss': stop_loss})
            else:
                raise Exception('stop_loss must lie in 0 - 100')
        except:
            raise Exception('stop_loss is not a number')
        try:
            profit_booking = float(profit_booking)
            if 0 <= profit_booking <= 100:
                self.criterion_dict.update({'profit_booking': profit_booking})
            else:
                raise Exception('profit_booking must lie in 0 - 100')
        except:
            raise Exception('profit_booking is not a number')
        self.criterion_dict.update({'enter_criterion': self.parse_criterion(enter_criterion)})
        self.criterion_dict.update({'exit_criterion': self.parse_criterion()(exit_criterion)})

    def parse_criterion(self, criterion):
        if criterion == None:
            return None

        criterion = criterion.lower().strip()
        """
        if or/and is absent, [[criterion]]
        if or is present, [[c1], [c2]]
        if and is present, [[c1, c2]]
        if and or are present, [[c1, c2], [c3, c4], [[c5], [c6]]]
        """
        criterion = [[i.strip()] for i in criterion.split('or')]
        criterion = [k[0].split('and') for k in criterion]
        criterion_temp = []
        for i in criterion:
            temp = []
            for j in i:
                temp.append(j.strip())
            criterion_temp.append(temp)
        criterion = criterion_temp

        split_criterion = None
        for operator in self.operators:
            if len(criterion.split(operator)) > 1:
                split_criterion = criterion.split(operator)
                break
            else:
                continue
        if split_criterion == None:
            raise Exception('Could not decode strategy operators')

StrategyCriterion(enter_criterion='ema(20) >= ema(10) or sma(20) >= sma(10) and ema(20) >= ema(10) or sma(20) >= sma(10) or ema(20) >= ema(10) and sma(20) >= sma(10)', stop_loss=10, profit_booking=10)

class StrategPerformance(object):
    def __init__(self):
        pass
