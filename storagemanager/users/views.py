from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Create new user
            form.save()

            # Automatically log in new user
            username = form.cleaned_data.get('username')
            new_user = authenticate(username=username,
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            messages.success(
                request, f'{username}, your account has been created.')

            # Add phone number to profile
            user = User.objects.get(username=username)
            profile = Profile.find_profile(user)
            phone_number = form.cleaned_data.get('phone_number')
            profile.add_phone_number(phone_number)

            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(
                request, 'Your account has been updated.')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    forms = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', forms)
