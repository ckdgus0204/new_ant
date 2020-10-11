from django.shortcuts import render, redirect
from .models import User
from .forms import UserLoginForm, UserSignupForm
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

# from .forms import CreateUserForm

# Create your views here.
def signup(request):
    if request.method == "POST":
        if request.POST["password"] == request.POST["password2"]:
            form = UserSignupForm(request.POST)
            
            print(form["password"])

            if form.is_valid():
                user = User()
                user = form.save(commit=False)
                user.password=make_password(user.password)
                user.save()
                auth.login(request,user)
                return redirect('home')
            else:
                form = UserSignupForm()
                print('form not valid')
                return render(request, 'registration/signup.html',{'form':form})
        else:
            form = UserSignupForm()
            print('비밀번호와 비밀번호 확인이 다름')
            return render(request, 'registration/signup.html',{'form':form})
    else:
        form = UserSignupForm()
        print('request not post')
        return render(request, 'registration/signup.html',{'form':form})
        
def login(request):
    if request.method=="POST":
        form=UserLoginForm(request.POST)
        username = request.POST.get('username')
        password=request.POST['password']
        user = auth.authenticate(username=username, password=password)
        print(request.POST['password'])
        print(user)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            print('user=none이래')
            return render(request, 'registration/login.html')

    else:
        print('POST_not')
        return render(request,'registration/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')
    