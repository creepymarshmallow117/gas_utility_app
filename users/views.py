from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

class CustomUserCreationForm(UserCreationForm):
    pan_number = forms.CharField(max_length =10, required=True, help_text="Enter your PAN number")

    class Meta:
        model = CustomUser
        fields = ['username', 
                    'email', 
                    'password1', 
                    'password2', 
                    'first_name', 
                    'last_name', 
                    'pan_number',
                    ]

    def clean_pan_number(self):
        pan_number = self.cleaned_data.get('pan_number')
        if not pan_number.isalnum() or len(pan_number) != 10:
            raise forms.ValidationError("PAN number must be 10 alphanumeric characters.")
        return pan_number

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registeration successful!")
            return redirect('create_request')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('redirect_based_on_role')
        else:
            messages.error(request, "Invalid username or password")
    
    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def redirect_based_on_role(request):
    if request.user.is_support_staff:
        return redirect('customer_support_dashboard')
    else:
        return redirect('consumer_service_dashboard')
