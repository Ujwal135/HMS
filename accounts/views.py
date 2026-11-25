from django.shortcuts import render,redirect
from django.contrib.auth.decorators import user_passes_test
from .forms import Accountcreationform

# Create your views here.
def create_account(request):
    
    if request.method == "POST":
        
        form = Accountcreationform(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('create_accounts')
    else:
        form = Accountcreationform()
    
    return render(
        request,
        'accounts/create_account.html',
        {"form":form}
        
    )