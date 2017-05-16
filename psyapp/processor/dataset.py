import numpy
import pandas as pd
from engine.drivers import feedapi

class Dataset(object):
    def __init__(self, secId, from_date, to_date, frequency):
        """
        secId = <type str>
        from_date, to_date = 'YYYY-MM-DD'
        frequency = minute, daily, hourly

        returns a DataFrame to be used in TechnicalIndicator classes
        """
        self.secId = secId
        self.from_date = from_date
        self.to_date = to_date
        self.frequency = frequency

        self.load_data()
        self.dataset()

    def load_data(self):
        self.price_list = feedapi.fetch_price_list(secId=self.secId,
                                              datefrom=self.from_date,
                                              dateto=self.to_date,
                                              frequency=self.frequency)
        self.price_list = [float(i) for i in self.price_list]

    def dataset(self):
        price_array = numpy.array(self.price_list)
        self.data_frame = pd.DataFrame({self.secId: price_array})
