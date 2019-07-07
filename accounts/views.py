from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirmPassword']:
            try:
                user = User.objects.get(username=request.POST['mobile'])
                return render(request, 'accounts/signup.html', {'error': 'Username Already has taken.'})
            except user.DoesNotExist:
                user = User.objects.create_user(first_name=request.POST['first_name'], last_name=request.POST['last_name'],username=request.POST['mobile'],password=request.POST['password'])
                auth.login(request,user)
                return redirect('home')

        else:
            return render(request, 'accounts/signup.html', {'error':'Password should be same.'})
    else:
        return render(request, 'accounts/signup.html')
    return render(request, 'accounts/signup.html')
