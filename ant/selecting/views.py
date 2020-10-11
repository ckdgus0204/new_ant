from django.shortcuts import render

# Create your views here.
def selecting_home(request):
    return render(request,'selecting/selecting_home.html')