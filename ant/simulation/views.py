from django.shortcuts import render, redirect
from datetime import datetime
from pandas_datareader import data 
from ergate.models import Simulation, Stockitem
from .forms import Add_SimulationForm
import yfinance as yf
import time
import pandas as pd

# Create your views here.
def simulation_home(request):
    yf.pdr_override()
    
    symbols = ['005930','000660','005935','207940','035420','068270','051910','005380','051900','028260','006400','012330','017670','036570','005490','035720','105560','055550','015760','034730'] #
    tm=time.strftime('%Y-%m-%d', time.localtime(time.time()))
    today=datetime.today()
    year=today.year
    month=today.month
    day=today.day
    
    # for i in symbols:
    #     chart_data = data.get_data_yahoo(
    #         i+'.KS', # KS : KOSPI, KQ : KOSDAQ
    #         tm
    #     )
    for i in symbols:
        try:
            stocklists=Simulation.objects.filter(st_num = i)
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

    mylists=Simulation.objects.filter(uname = request.user)
    context={'mylists':mylists,'year':year,'month':month,'day':day}
    return render(request,'simulation/simulation_home.html',context)

def simulation_select(request):
    return render(request,'simulation/simulation_select.html')

def add_Simulation(request):
    today=datetime.today()
    year=today.year
    month=today.month
    day=today.day
    if request.method == "POST":
        print(request.user)
        print(request.POST["sname"])
        mylists=Stockitem.objects.get(name = request.POST["sname"])
        print(mylists)
        print(mylists.stock_num)
        if mylists is not  None:
            form = Add_SimulationForm(request.POST)
            if form.is_valid():
                simulation = Simulation()
                simulation = form.save(commit=False)
                simulation.st_num=mylists
                simulation.sname=mylists.name
                simulation.uname=request.user
                simulation.today=simulation.input
                simulation.save()
                mylists=Simulation.objects.filter(uname = request.user)
                context={'mylists':mylists,'year':year,'month':month,'day':day}
                return render(request,'simulation/simulation_home.html',context)
            else:
                form = Add_SimulationForm()
                print('form not valid')
                return render(request, 'home.html',{'form':form})
        else:
            form = Add_SimulationForm()
            print('비밀번호와 비밀번호 확인이 다름')
            return render(request,  'home.html',{'form':form})
    else:
        form = Add_SimulationForm()
        print('request not post')
        return render(request, 'home.html',{'form':form})
        