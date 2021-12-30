from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import (UserRegisterForm, LoginForm, UserUpdateForm, ProfileUpdateForm, )
from django.contrib import messages
from .backends import CustomAuthBackend
from .models import Profile
from django.contrib.auth import login as auth_login
from django.contrib.auth import views as auth_views


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'You have successfully registered to XPENCE!')
            return redirect('users:login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/signup.html', {'form': form})


def login(request):
    context = {}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        email = request.POST['email']
        # phone = request.POST['phone']
        password = request.POST['password']
        user = CustomAuthBackend.authenticate(self=request,
                                              email=email,
                                              password=password)
        if user:
            if user.is_active:
                auth_login(request, user, backend='users.backends.CustomAuthBackend')
                return redirect(request.GET.get('next') or reverse('core:home'))
        else:
            messages.error(request, f'Please enter the correct email and password. '
                                    f'Note that both fields might be case sensitive.')
            return redirect(reverse('users:login'))
    else:
        form = LoginForm()
        toggled = request.GET.get('login_with_phone')
        context = {'form': form, 'title': 'Login'}
    return render(request, 'users/login.html', context)


def profile(request):
    user_profile = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Successfully updated your profile!')
            return redirect('users:profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'title': 'Profile'
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    context = {'title': 'Logged Out'}
    return render(request, 'users/logout.html', context)
