from django.shortcuts import render
from datetime import datetime
from pandas_datareader import data as pdr
import yfinance as yf

yf.pdr_override()
import pandas as pd

# Create your views here.
def simulation_home(request):
    day=datetime.today()        # 현재 일 가져오기
    date={'day':day}

    stock=pdr.get_data_yahoo('005930.KS','2020-06-17')

    #print(stock)
    #stock_price=stock.get_price()
    #stock_time=stock.get_trade_datetime()
    #context={'day':day,'stock_price':stock_price,'stock_time':stock_time}
    return render(request,'simulation/simulation_home.html',{'stock':stock})
def simulation_select(request):

    return render(request,'simulation/simulation_select.html')

    