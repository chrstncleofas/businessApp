# views.py
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

def home(request):
    return render(request, 'businessApp/index.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST['login-username']
        password = request.POST['login-password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            # fname = user.first_name
            messages.success(request, "Logged In Sucessfully!!")
            # return render(request, 'authentication/dashboard.html')
            # return render(request, "authentication/dashboard.html",{"fname":fname})
            return redirect('dashboard')
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('dashboard')

    return render(request, 'businessApp/login.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('signup-username')
        email = request.POST.get('signup-email')
        password = request.POST.get('signup-password')

        myuser = User.objects.create_user(username, email, password)
        myuser.save()

        # Add a context variable to indicate successful registration
        context = {
            'registration_successful': True,
        }

        return render(request, 'businessApp/register.html', context)

    return render(request, 'businessApp/register.html')

def dashboard(request):
    return render(request, 'businessApp/dashboard.html')
