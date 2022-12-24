from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm

# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("chat")
        else:
            messages.error(request, "Error occurred, complete the form with valid fields.")
            return redirect("login")
    else:
        return render(request, "authenticate/login.html")

def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("chat")
        else:
            messages.error(request, "Error occurred, complete the form with valid fields.")
            return redirect("register")
    else:
        context = {"type": "register", "form": form}
        return render(request, "authenticate/register.html", context)

@login_required(login_url="login")
def logout_user(request):
    logout(request)
    messages.success(request, "You were logged out.")
    return redirect("login")