# from psyapp.settings import LUIS_API
import requests

import technical_indicators as tis

LUIS_API = 'https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/eb9c8257-04a7-4532-8912-fe2f6e1baf18?subscription-key=677b4af032664caa8295a1d214c9d887&staging=true&verbose=true&timezoneOffset=0&q='

ALLOWED_TI = {
    'simple moving average': 'SMA',
    'exponential moving average': 'EMA',
    'open': 'Open',
    'high': 'High',
    'low': 'Low',
    'close': 'Close',
    'rsi': 'RSI',
    'atr': 'ATR'
}

def nlu_model(strategy_text, secId, df):
    # if not isinstance(strategy_text, basestring):
    #     raise Exception('Unknownn strategy_text format. Allowed unicode or string.')
    # luis_response = requests.get(LUIS_API + strategy_text)
    # luis_response = luis_response.json()
    # if luis_response['topScoringIntent']['intent'] != 'strategy_condition':
    #     # Implement what happens if 'intent' is not a startegy
    #     raise Exception('intent is not a strategy')
    # for intent in luis_response['intents']:
    #     if intent['intent'] == 'startegy_condition':
    #         if intent['score'] < 0.9:
    #             # Implement what happenns if predictibility is less than 90%
    #             raise Exception('intent score less than 0.9')

    """
    For demo purpose only
    """
    words_list = strategy_text.split()
    words_list[1] = ordinal_to_seconds(words_list[1])
    words_list[-2] = ordinal_to_seconds(words_list[-2])
    args = [int(words_list[0]), int(words_list[-3])]
    ti = [words_list[2], words_list[-1]]

    up_relation = ['crosses above', 'exceeds']
    below_relation = ['crosses below', 'goes below']
    equal_relation = ['equals', 'touches', 'equals to', 'equal', 'reaches']

    if words_list[3:-3] in up_relation:
        cmp = '>'
    elif words_list[3:-3] in below_relation:
        cmp = '<'
    elif words_list[3:-3] in equal_relation:
        cmp = '=='

    ti[0] = tiText_to_tiSym(ti[0])
    ti[1] = tiText_to_tiSym(ti[1])

    df = getattr(tis, ti[0])(secId, args[0]).results(df)
    df = getattr(tis, ti[1])(secId, args[1]).results(df)

    return df

def validate_text(strategy_text):
    """
    For demo purpose only
    """
    words_list = strategy_text.split()
    try:
        words_list[1] = ordinal_to_seconds(words_list[1])
        words_list[-2] = ordinal_to_seconds(words_list[-2])
        args = [int(words_list[0]) * words_list[1], int(words_list[-3]) * words_list[-2]]
        ti = [words_list[2], words_list[-1]]

        up_relation = ['crosses_above', 'exceeds']
        below_relation = ['crosses_below', 'goes_below']
        equal_relation = ['equals', 'touches', 'equals_to', 'equal', 'reaches']

        if words_list[3:-3][0] in up_relation:
            cmp = '>'
        elif words_list[3:-3][0] in below_relation:
            cmp = '<'
        elif words_list[3:-3][0] in equal_relation:
            cmp = '=='

        ti[0] = tiText_to_tiSym(ti[0])
        ti[1] = tiText_to_tiSym(ti[1])

        return True
    except:
        return False

def ordinal_to_seconds(ordinal):
    if ordinal == 'week' or ordinal == 'weeks':
        return 604800
    elif ordinal == 'day' or ordinal == 'days':
        return 86400
    elif ordinal == 'hour' or ordinal == 'hours':
        return 3600
    elif ordinal == 'minute' or ordinal == 'minutes':
        return 60

def tiText_to_tiSym(ti):
    if ti.lower() == 'simple_moving_average':
        return 'SMA'
    elif ti.lower() == 'exponential_moving_average':
        return 'EMA'
    elif ri.lower() == 'rsi' or ri.lower() == 'relative_strength_index':
        return 'RSI'
    elif ri.lower() == 'rate_of_change' or ri.lower() == 'change':
        return 'ROC'
