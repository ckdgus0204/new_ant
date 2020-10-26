from pandas_datareader import data
import yfinance as yf
import pandas as pd

yf.pdr_override()
# Samsung
ticker = "005930.KS" # KS : KOSPI, KQ : KOSDAQ

chart_data = data.get_data_yahoo(
	ticker, 
	'2020-01-01', # start
	'2020-01-30' # end
)
print (chart_data)
print (type(chart_data))

# save
# chart_data.to_csv ("./"+ticker+".csv", index=True, header=True)