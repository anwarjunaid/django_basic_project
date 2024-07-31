from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm  # Imported custom form
from django.views.decorators.cache import never_cache

# Create your views here.
def signupView(request):
    if request.method == 'POST':
        # print("thik hai yahan tak")
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print("yes valid")
            user = form.save(commit=False)
            user.email = form.cleaned_data.get('email')
            user.save()
            login(request, user)
            return redirect('dashboard')
    else:
        inital_data = {'username':'', 'email':'', 'password1':'', 'password2':''}
        form = CustomUserCreationForm(initial = inital_data)
    return render(request, 'signup.html', {'form': form})

@never_cache
def signinView(request):
    if request.method == 'POST':
        # print("thik hai yahan tak")
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            print("yes valid")
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
        else:
            print("Form errors : ",form.errors)
    else:
        inital_data = {'username':'', 'password':''}
        form = AuthenticationForm(initial = inital_data)
    return render(request, 'signin.html', {'form': form})

def dashboardView(request):
    return render(request, 'dashboard.html')

def logoutView(request):
    logout(request)
    return redirect('login')
