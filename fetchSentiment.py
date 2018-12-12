# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 20:21:16 2018
This program gets the stock quotes for given tickers & writes them to csv file
Source: quandl
@author: siva
"""

import quandl
quandl.ApiConfig.api_key = 'TyiXJXHTBB9SG2-GZPvC'

# get the table for daily stock prices and,
# filter the table for selected tickers, columns within a time range
# set paginate to True because Quandl limits tables API to 10,000 rows per call

#
from_date = "2014-01-01"
to_date = "2018-12-31"

#sentiment indicator
sentiment = quandl.get('AAII/AAII_SENTIMENT',start_date=from_date,end_date=to_date)

#Write the data to csv file.
