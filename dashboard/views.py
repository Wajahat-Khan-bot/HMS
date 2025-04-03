from django.shortcuts import render, redirect
from client.views import client_list
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')
