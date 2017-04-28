import string
import json
import pdb
import re, math
from collections import Counter

# from .models import Indicators
# from indicators import ema
#
# from nltk.tokenize.api import TokenizerI
# import nltk.corpus
# import nltk.tokenize.punkt
# import nltk.stem.snowball
# import string
#
# # Get default English stopwords and extend with punctuation
# stopwords = nltk.corpus.stopwords.words('english')
# stopwords.extend(string.punctuation)
# stopwords.append('')
#
# # Create tokenizer and stemmer
# print dir(TokenizerI.tokenize)
# tokenizer = TokenizerI()
#
# def is_ci_token_stopword_set_match(a, b, threshold=0.5):
#     """Check if a and b are matches."""
#     tokens_a = [token.lower().strip(string.punctuation) for token in tokenizer.span_tokenize(a) \
#                     if token.lower().strip(string.punctuation) not in stopwords]
#     tokens_b = [token.lower().strip(string.punctuation) for token in tokenizer.span_tokenize(b) \
#                     if token.lower().strip(string.punctuation) not in stopwords]
#
#     # Calculate Jaccard similarity
#     ratio = len(set(tokens_a).intersection(tokens_b)) / float(len(set(tokens_a).union(tokens_b)))
#     return (ratio >= threshold)
#
# a = '20 days exponential moving average crosses above 10 days exponential moving average by 20%'
# b = '20 days exponential moving average crosses below 10 days exponential moving average by 20%'
#
# is_ci_token_stopword_set_match(a, b)

# WORD = re.compile(r'\w+')
#
# def get_cosine(vec1, vec2):
#      intersection = set(vec1.keys()) & set(vec2.keys())
#      numerator = sum([vec1[x] * vec2[x] for x in intersection])
#
#      sum1 = sum([vec1[x]**2 for x in vec1.keys()])
#      sum2 = sum([vec2[x]**2 for x in vec2.keys()])
#      denominator = math.sqrt(sum1) * math.sqrt(sum2)
#
#      if not denominator:
#         return 0.0
#      else:
#         return float(numerator) / denominator
#
# def text_to_vector(text):
#      words = WORD.findall(text)
#      return Counter(words)
#
# text1 = '20 days exponential moving average crosses above 10 days exponential moving average by 20%'
# text2 = '20 days exponential moving average crosses below 10 days exponential moving average by 20%'
#
# vector1 = text_to_vector(text1)
# vector2 = text_to_vector(text2)
#
# cosine = get_cosine(vector1, vector2)
#
# print 'Cosine:', cosine


class NLPService(object):
    # indicators = Indicators.objects.filter()
    indicators = ['upper_bollinger_band', 'lower_bollinger_band', 'current_price', 'open_interest', 'volume', 'close_price', 'open_price', 'lowest_price', 'highest_price', 'stochastic_oscillator', 'rate_of_change', 'on_balance_volume', 'money_flow_index', 'moving_average_convergence_divergence', 'relative_strength_index', 'moving_average', 'exponential_moving_average', 'average_directional_index']

    condition  = ['crosses below', 'crosses above', 'higher than', 'touches', 'lower than', 'equal to', 'below', 'above', 'greater than', 'less than']

    verb = ['is', 'are']

    frequency = ['minute', 'hour', 'day', 'week', 'month']

    rule = "%s %s "

    def __init__(self, strategy):
        # condition = {
        #     'condition': 'ma(rsi(14)) > rsi(14)*1.1'
        # }
        # return json.dumps(condition)
        self.parseStrategy(strategy)

    def parseStrategy(self, strategy):
        """
        Input: text strategey
        Output: strategy function
        For Example,
        Input: 20 days exponential moving average crosses above 10 days exponential moving average by 20%
        Output: ema(20)
        """
        strategy = strategy.translate(None, string.punctuation)
        print strategy

# NLPService(strategy="volume is 10 times higher than. previous month average volume")
