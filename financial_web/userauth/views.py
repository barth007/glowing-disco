from django.shortcuts import render, redirect
from userauth.form import RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from userauth.models import User


@csrf_protect
def register_view(request):
    """registers user

    Args:
    --- request(obj)
    Return:
    --- A rendered page
    """

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f"Hi, {username} your account was created successfully."
            )
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            if new_user:
                login(request, new_user)
            return redirect('account:account')
    elif request.user.is_authenticated:
        messages.warning(
            request, f"You're already logged in."
        )
        return redirect('account:account')
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }

    return render(request, 'auth/sign-up.html', context)


@csrf_protect
def login_view(request):
    """ logging requested users in"""

    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You are logged in")
                return redirect('account:account')
            else:
                messages.warning(
                    request, "Username or password does not exits")
                return redirect('userauth:sign-in')
        except User.DoesNotExist:
            messages.warning(request, "User does not exits")
            return redirect('userauth:sign-in')

    return render(request, 'auth/sign-in.html')


def logout_view(request):
    """logging the user out"""

    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('userauth:sign-in')
