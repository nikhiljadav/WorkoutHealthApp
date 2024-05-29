from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm


# Create your views here.
def registration_view(request):
    context = {}

    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'account/register.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')

def login_view(request):
    context = {}

    user = request.user                                         #gets user from request
    if user.is_authenticated:                                   #checks if already authenticated
        return redirect("home")                                 #if alr authenticated, redirect to home
    
    if request.POST:                                            #check if form has been submitted
        form = AccountAuthenticationForm(request.POST)          #make instance of the authentication form w/ the submitted data
        if form.is_valid():                                     #if the form is valid, get the cleaned data
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password) #authenticate the user with the given email and password

            if user:                                            #if authentication is successful, login the user and redirect to home page
                login(request, user)
                return redirect("home")
    else:
        form = AccountAuthenticationForm()                      #if request method is get, make an empty form
    
    context['login_form'] = form                                #if form isnt valid, this leads to the validation error in the forms.py
    return render(request, 'account/login.html', context)

def account_view(request):
    if not request.user.is_authenticated:
        return redirect("login")

    context = {}

    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.initial = {
                "email": request.POST["email"],
                "username": request.POST["username"]
            }
            form.save()
            context['success_message'] = "Updated"
    else:
        form = AccountUpdateForm(
            initial= {
                "email": request.user.email,
                "username": request.user.username,
            }
        )
    context['account_form'] = form
    return render(request, 'account/account.html', context)