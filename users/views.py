from django.shortcuts import render, redirect
from users.forms import CustomUserForm, LoginForm
from django.contrib.auth import authenticate, login
from django.views.decorators.cache import cache_control


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')  
    else:
        form = CustomUserForm()
    return render(request, 'users/signup.html', {'form': form})



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('core:home') 
    else:
        form = LoginForm()
    
    return render(request, 'users/login.html', {'form': form})


