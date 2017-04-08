import json

def slprocessor(strategy):
    condition = {
        'condition': 'ma(rsi(14)) > rsi(14)*1.1'
    }
    return json.dumps(condition)
