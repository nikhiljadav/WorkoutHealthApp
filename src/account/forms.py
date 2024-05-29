from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from account.models import Account

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')

    class Meta:
        model = Account
        fields = ("email", "username", "password1", "password2")
    
class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')
    
    def clean(self):                                                #add custom validation logic
        if self.is_valid():                                         #if form passed initial validation, retrive the cleaned data
            email = self.cleaned_data['email']                      #self.cleaned_data is a dictionary that has validated data so far
            password = self.cleaned_data['password']                #you can retrive the email and password which are stored in the dictionary
            if not authenticate(email=email, password=password):    #attempt to authenticate the user
                raise forms.ValidationError("Invalid Login")        #it gives a validation error message if its not valid

class AccountUpdateForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = {'email', 'username'}

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:        #tries to get an account with the same email but a different primary key
                account = Account.objects.exclude(pk = self.instance.pk).get(email=email) #checking to see if acccount exists
            except Account.DoesNotExist:        #if account does not exist return the email
                return email
            raise forms.ValidationError('Email "%s" is already in use.' % email)        #if account does exist, then raise a validation error

    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                account = Account.objects.exclude(pk = self.instance.pk).get(username=username) #checking to see if acccount exists
            except Account.DoesNotExist:
                return username
            raise forms.ValidationError('Username "%s" is already in use.' % username)
