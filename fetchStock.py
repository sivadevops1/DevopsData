# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 20:21:16 2018
This program gets the stock quotes for given tickers & writes them to csv file
Source: quandl
@author: siva
"""

import quandl
import pandas as pd

quandl.ApiConfig.api_key = 'TyiXJXHTBB9SG2-GZPvC'

# get the table for daily stock prices and,
# filter the table for selected tickers, columns within a time range
# set paginate to True because Quandl limits tables API to 10,000 rows per call

#
from_date = "2015-01-01"
to_date = "2018-01-31"
csv_folder = 'C:\\Users\\sivas\\Python Projects\\DevopsData\\data\\'

#Folder name where csv should be written

#Pull all the data for the required stocks
tcs_raw = quandl.get('NSE/TCS', start_date = from_date, end_date=to_date)
tcs = tcs_raw.iloc[:,[0,1,2,4,5]]
tcs['Stock'] = 'TCS'
tcs.columns = ['Open', 'High', 'Low', 'Close','Volume','Stock']
tcs=tcs[['Stock','Open', 'High', 'Low', 'Close','Volume']]
tcs.to_csv(csv_folder+"tcs.csv")

#TATAMOTORS
tatamotors_raw = quandl.get('NSE/TATAMOTORS', start_date = from_date, end_date=to_date)
tatamotors = tatamotors_raw.iloc[:,[0,1,2,4,5]]
tatamotors['Stock'] = 'TATAMOTORS'
tatamotors.columns = ['Open', 'High', 'Low', 'Close','Volume','Stock']
tatamotors=tatamotors[['Stock','Open', 'High', 'Low', 'Close','Volume']]
tatamotors.to_csv(csv_folder+"tatamotors.csv")

#TATASTEEL
tatasteel_raw = quandl.get('NSE/TATASTEEL', start_date = from_date, end_date=to_date)
tatasteel = tatasteel_raw.iloc[:,[0,1,2,4,5]]
tatasteel['Stock'] = 'TATASTEEL'
tatasteel.columns = ['Open', 'High', 'Low', 'Close','Volume','Stock']
tatasteel=tatasteel[['Stock','Open', 'High', 'Low', 'Close','Volume']]
tatasteel.to_csv(csv_folder+"tatasteel.csv")

#TATACOFFEE
tatacoffee_raw = quandl.get('NSE/TATACOFFEE', start_date = from_date, end_date=to_date)
tatacoffee = tatacoffee_raw.iloc[:,[0,1,2,4,5]]
tatacoffee['Stock'] = 'TATACOFFEE'
tatacoffee.columns = ['Open', 'High', 'Low', 'Close','Volume','Stock']
tatacoffee=tatacoffee[['Stock','Open', 'High', 'Low', 'Close','Volume']]
tatacoffee.to_csv(csv_folder+"tatacoffee.csv")

#TITAN
titan_raw = quandl.get('NSE/TITAN', start_date = from_date, end_date=to_date)
titan = titan_raw.iloc[:,[0,1,2,4,5]]
titan['Stock'] = 'TITAN'
titan.columns = ['Open', 'High', 'Low', 'Close','Volume','Stock']
titan=titan[['Stock','Open', 'High', 'Low', 'Close','Volume']]
titan.to_csv(csv_folder+"titan.csv")

#Merge all to one
frames=[tcs,tatamotors,tatasteel,tatacoffee,titan]
all_stocks=pd.concat(frames)
all_stocks.to_csv(csv_folder+"all_stocks.csv")

#Add a column to the prices & change the column names
#Fetch sentiment indicator, merge it with the 
sentiment_raw = quandl.get('AAII/AAII_SENTIMENT',start_date=from_date,end_date=to_date)
sentiment = sentiment_raw.iloc[:,[0,1,2]]
res1=all_stocks.join(sentiment)
res1 = res1.fillna(method='backfill')
res1.to_csv(csv_folder+"all_sentimet.csv")


#Currency
df = pd.read_csv(csv_folder+"USDINR.csv")
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
df.columns = ['USDINR']
res2=res1.join(df)
res2.to_csv(csv_folder+"all_sentimet_fx.csv")






