from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login, logout

def sign_up(request):
    if request.method == ('POST'):
        print('POST: ', request.POST)
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username = username).exists():
            messages.error(request,"Username already taken.")
            return redirect("sign_up")
        if User.objects.filter(email= email).exists():
            messages.error(request, "Email is already registered.")
            return redirect('sign_up')
        
        user = User.objects.create_user(username = username, email = email, password = password)
        user.save()

        messages.success(request, "Signup successful! You can now log in.")
        return redirect("log_in")

    return render(request, 'accounts/sign_up.html')

def log_in(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "login successful!")
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'accounts/log_in.html')

def log_out(request):
    logout(request)
    return redirect('log_in')