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
        enter_criterion: <type str> 'ema(20) >= sma(10) and/or ema(20) >= sma(10)'
        exit_criterion: <type str> 'ema(20) >= sma(10) and/or ema(20) >= sma(10)'
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

    def parse_criterion(criterion):
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

class StrategPerformance(object):
    def __init__(self):
        pass
    def sharpe_ratio(self):
        """
        Sharpe ratio = (Mean return − Risk-free rate)/Standard deviation
        higher sharpe ratio is better
        input parameters: mean_return, riskfree_rate, std_dev
        return: float value (0<x<1)
        """
        pass
    def sortino_ratio(self):
        """
        Sortino ratio=(Expected return - Risk-free rate of return)/Standard deviation of negative assests returns
        higher Sortino ratio is better.
        input parameters: exp_return, riskfree_rate, std_dev
        return: float value (0<x<1)
        """
        pass
    def max_drawdown(self):
        """
        Maximum Drawdown is expressed in percentage terms and computed as:
        (Trough Value – Peak Value) ÷ Peak Value
        input: through_value, peak_value
        return: float value (0<x<1)
        """
        pass
    def cagr(self):
        """
        Maximum Drawdown is expressed in percentage terms and computed as:
        (Ending value/ Beginning value)^(1/ number of years) -1
        input: end_value, beg_value, years
        return: float value (0<x<1)
        """
        pass
    def winning_rate(self):
        """
        Win Rate = Number of Impressions Won/ Number of Impressions Bid
        input: won, total_bid
        return: float value (0<x<1)
        """
        pass
    def losing_rate(self):
        """
        Win Rate = Number of Impressions Won/ Number of Impressions Bid
        input: loss, total_bid
        return: float value (0<x<1)
        """
        pass
