from cgi import print_arguments
from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

from .models import UserProfile
# Create your views here.

def LoginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print("User: ", user)
        if user is not None:
            print('User is authenticated')
            login(request, user)
            print('User is logged in')
            current_user = request.user
            userprofile = UserProfile.objects.get(user_id=current_user.id)
            print('UserProfile: ', userprofile)
            return HttpResponseRedirect(reverse('IndexView'))
        else:
            messages.warning(
                request, "Login error! Username or Password is wrong.")
            # send error message
            return HttpResponseRedirect(reverse('LoginView'))
    else:
        return render(request, 'Log_in.html')



def SignupView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            print('Username already exists')
            messages.warning(
                request, "Username already exists.")
            # send error message
            return HttpResponseRedirect(reverse('SignupView'))
        else:
            print('Username is available')
            user = User.objects.create_user(username=username, password=password)
            user.save()
            print('User created')
            userprofile = UserProfile.objects.create(user=user)
            userprofile.save()
            print('UserProfile created')
            login(request, user)
            return HttpResponseRedirect(reverse('IndexView'))
    else:
        return render(request, 'Sign_In.html')

def LogoutView(request):
    logout(request)
    print('User is logged out')
    return HttpResponseRedirect(reverse('IndexView'))