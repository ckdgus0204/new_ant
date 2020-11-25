from django.shortcuts import render, redirect
from rest_framework.response import Response
import yfinance as yf
import time
from pandas_datareader import data
from rest_framework.views import APIView
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Autoset
# Create your views here.
def home(request):
    return render(request,'home.html')

def trading_home(request):
    mylists=Autoset.objects.filter(uname = request.user)
    return render(request,'trading_home.html',{'mylists':mylists})

def trading_end(request):

    if request.method == "POST":
        print(request.POST)
    mylists=Autoset.objects.get(auto_num = request.POST["mylist"])
    mylists.end_date=time.strftime('%Y%m%d', time.localtime(time.time()))
    mylists.save()

    newlists=Autoset.objects.filter(uname = request.user)
    return render(request,'trading_home.html',{'mylists':newlists})


def mypage(request):
    yf.pdr_override()
    
    symbols = ['005930','000660','005935','207940','035420','068270','051910','005380','051900','028260','006400','012330','017670','036570','005490','035720','105560','055550','015760','034730'] #
    tm=time.strftime('%Y-%m-%d', time.localtime(time.time()))

    # for i in symbols:
    #     chart_data = data.get_data_yahoo(
    #         i+'.KS', # KS : KOSPI, KQ : KOSDAQ
    #         tm
    #     )
    for i in symbols:
        try:
            stocklists=Autoset.objects.filter(s_num = i)
            for stocklist in stocklists:
                chart_data = data.get_data_yahoo(
                    i+'.KS', # KS : KOSPI, KQ : KOSDAQ
                    tm
                )
                stocklist.today=chart_data.loc[chart_data.index[len(chart_data.index)-1], 'Close']
                print(stocklist)
                stocklist.save()
        except: #refresh stockitem.today
            print('pass됨')

    mylists=Autoset.objects.filter(uname = request.user)
    count=0
    request.user.before_account=0
    request.user.account=0
    for mylist in mylists:
        print(mylist)
        print(mylist.today)
        request.user.account=((request.user.account)+mylist.today)
        request.user.before_account=request.user.before_account+mylist.input
    request.user.total_profit=request.user.account-request.user.before_account
    
    try:
        request.user.profit_percent=(request.user.total_profit/request.user.account)*100
    # ZeroDivisionError
    except:     
        request.user.profit_percent=0
    
    return render(request,'mypage.html',{'mylists':mylists})
