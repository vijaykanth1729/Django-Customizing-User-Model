from django.shortcuts import render, redirect


from .forms import RegistrationForm, LoginForm, AccountUpdateForm
from . models import Account
from django.contrib.auth import login, authenticate, logout

def registration(request):
    context = {}
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # email = form.cleaned_data.get('email')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(email=email, password=raw_password)
            #login(request, account)
            return render(request,'account/success_registration.html')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form

    return render(request,'account/register.html' , context)


def logout_view(request):
    logout(request)
    return redirect('home')

def login_view(request):
    context = {}
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('portfolio')
    else:
        form = LoginForm()
    context['Login_form'] = form
    return render(request, 'account/login.html', context)


def account_view(request):
    context = {}
    if request.method == "POST":
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return render(request, 'account/success_account.html')
    else:
        form = AccountUpdateForm(
            initial = {
                'email':request.user.email,
                'username': request.user.username,
            }
        )
    context['account_form'] = form

    return render(request, 'account/account.html', context)


