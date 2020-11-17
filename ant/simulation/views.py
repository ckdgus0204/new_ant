from django.shortcuts import render
from datetime import datetime
from pandas_datareader import data as pdr
from ergate.models import Simulation
import yfinance as yf

yf.pdr_override()
import pandas as pd

# Create your views here.
def simulation_home(request):
    mylists=Simulation.objects.filter(uname = request.user)
    return render(request,'simulation/simulation_home.html',{'mylists':mylists})

def simulation_select(request):
    return render(request,'simulation/simulation_select.html')

    