from django.shortcuts import render, get_object_or_404
from account.models import Account


# Create your views here.

#homescreen view
def home_screen_view(request):
    
    context = {}

    accounts = Account.objects.all()
    context['accounts'] = accounts
    

    return render(request, "personal/home.html", context) 
    #already looking at templates