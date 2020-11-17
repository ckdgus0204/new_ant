from django.shortcuts import render, redirect
from rest_framework.response import Response
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


def mypage(request):
    mylists=Autoset.objects.filter(uname = request.user)
    count=0
    request.user.before_account=0
    request.user.account=0
    for mylist in mylists:
        request.user.account=((request.user.account)+mylist.today)
        request.user.before_account=request.user.before_account+mylist.input
    request.user.total_profit=request.user.account-request.user.before_account
    
    try:
        request.user.profit_percent=(request.user.total_profit/request.user.account)*100
    # ZeroDivisionError
    except:     
        request.user.profit_percent=0
    
    return render(request,'mypage.html',{'mylists':mylists})
