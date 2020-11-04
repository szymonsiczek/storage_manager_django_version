from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .forms import UserRegisterForm, UserUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        with transaction.atomic():
            if form.is_valid():
                # Create new user
                form.save()
                # Automatically log in new user
                user_mail = form.cleaned_data['email']
                new_user = authenticate(username=user_mail,
                                        password=form.cleaned_data['password1'],
                                        )
                login(request, new_user)
                user_full_name = form.cleaned_data['full_name']
                messages.success(
                    request, f'{user_full_name}, your account has been created.')
                return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(
            request.POST, request.FILES, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(
                request, 'Your account has been updated.')
            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
    forms = {
        'user_form': user_form
    }
    return render(request, 'users/profile_update.html', forms)


@login_required
def profile(request):
    return render(request, 'users/profile.html')
