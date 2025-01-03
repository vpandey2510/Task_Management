# Create your views here.

from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Save the user
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            
            # Authenticate user
            user = authenticate(username=username, password=password)
            messages.success(request, 'Registration was successful! Please log in.')
            return redirect('register')
        
        else:
            # Print form errors to the console
            print(messages.error)
            print(form.errors)
            messages.error(request, 'There was an error with your registration.')
    
    else:
        form = UserRegisterForm()
    
    return render(request, 'user/register.html', {'form': form})

    
def login_view(request):
    # if request.user.is_authenticated:
    #     return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                print(messages.success(request, f"Welcome, {username}! You have successfully logged in."))
                return redirect('home')  # Redirect to the homepage or any other page
            else:
                print(messages.error)
                messages.error(request, "Invalid username or password.")
        else:
            print(messages.error)
            messages.error(request, "Invalid username or password.")
    
    else:
        # For GET request, just create an empty login form
        form = AuthenticationForm()

    
    return render(request, 'user/login.html', {'form': form})

    
def profile(request):
    # pass

    return render(request, 'user/profile.html', {'user': request.user})



