from django.shortcuts import render, redirect
import yfinance as yf
import pandas as pd
from pandas_datareader import data
from ergate.models import Stockitem, Autoset
from .forms import Add_AutosetForm
import time

# Create your views here.
def selecting_home(request):
    return render(request,'selecting/selecting_home.html')
    
def reflash(request):
    yf.pdr_override()
    
    symbols = ['005930','000660','005935','207940','035420','068270','051910','005380','051900','028260','006400','012330','017670','036570','005490','035720','105560','055550','015760','034730'] #
    tm=time.strftime('%Y-%m-%d', time.localtime(time.time()))

    for i in symbols:
        chart_data = data.get_data_yahoo(
            i+'.KS', # KS : KOSPI, KQ : KOSDAQ
            '2020-01-01', # start
            tm
        )
        try:
            stocklists=Autoset.objects.filter(s_num = i)
            for stocklist in stocklists:
                stocklist.today=chart_data.loc[chart_data.index[len(chart_data.index)-1], 'Close']
                stocklist.save()
        except: #refresh stockitem.today
            pass
        chart_data.to_csv ("./static/data/"+i+".csv", index=True, header=True)    #save csv

    return render(request,'selecting/selecting_home.html')

def add_Autoset(request):
    if request.method == "POST":
        print(request.user)
        print(request.POST["sname"])
        mylists=Stockitem.objects.get(name = request.POST["sname"])
        print(mylists)
        print(mylists.stock_num)
        if mylists is not  None:
            form = Add_AutosetForm(request.POST)
            if form.is_valid():
                autoset = Autoset()
                autoset = form.save(commit=False)
                autoset.s_num=mylists
                autoset.sname=mylists.name
                autoset.uname=request.user
                
                autoset.save()
                return redirect('selecting_home')
            else:
                form = Add_AutosetForm()
                print('form not valid')
                return render(request, 'home.html',{'form':form})
        else:
            form = Add_AutosetForm()
            print('비밀번호와 비밀번호 확인이 다름')
            return render(request,  'home.html',{'form':form})
    else:
        form = Add_AutosetForm()
        print('request not post')
        return render(request, 'home.html',{'form':form})
        