from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request,'home.html')
def trading_home(request):
    return render(request,'trading_home.html')
def mypage(request):
    return render(request,'mypage.html')
