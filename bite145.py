from collections import namedtuple
from datetime import date

import pandas as pd

DATA_FILE = "weather-ann-arbor.csv"
STATION = namedtuple("Station", "ID Date Value")


def high_low_record_breakers_for_2015():
    """Extract the high and low record breaking temperatures for 2015

    The expected value will be a tuple with the highest and lowest record
    breaking temperatures for 2015 as compared to the temperature data
    provided.

    NOTE:
    The date values should not have any timestamps, should be a datetime.date() object.
    The temperatures in the dataset are in tenths of degrees Celsius, so you must divide them by 10

    Possible way to tackle this challenge:

    1. Create a DataFrame from the DATA_FILE dataset.
    2. Manipulate the data to extract the following:
       * Extract highest temperatures for each day between 2005-2015
       * Extract lowest temperatures for each day between 2005-2015
       * Remove February 29th from the dataset to work with only 365 days
    3. Separate data into two separate DataFrames:
       * high/low temperatures between 2005-2014
       * high/low temperatures for 2015
    4. Iterate over the 2005-2014 data and compare to the 2015 data:
       * For any temperature that is higher/lower in 2015 extract ID, Date, Value
    5. From the record breakers in 2015, extract the high/low of all the temperatures
       * Return those as STATION namedtuples, (high_2015, low_2015)
    """
    records = pd.read_csv(DATA_FILE, index_col='Date', parse_dates=['Date'])
    record_2015 = records['2015']
    max_min = record_2015.sort_values(by='Data_Value').reset_index()
    max_rec = max_min.iloc[-1]
    min_rec = max_min.iloc[0]

    max_record = STATION(max_rec.ID, max_rec.Date.date(),  max_rec.Data_Value/ 10)
    min_record = STATION(min_rec.ID, min_rec.Date.date(),  min_rec.Data_Value/ 10)
    return (max_record, min_record)

print(high_low_record_breakers_for_2015())