from django.shortcuts import render,redirect
from django.contrib.auth.decorators import user_passes_test
from .forms import Accountcreationform,Userloginform
from django.contrib.auth import login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
    # Create your views here.
    
    
    
def create_account(request):
        
        if request.method == "POST":
            
            form = Accountcreationform(request.POST)
            
            if form.is_valid():
                form.save()
                return redirect('login_page')
        else:
            form = Accountcreationform()
        
        return render(
            request,
            'accounts/create_account.html',
            {"form":form}
            
        )
        
def user_login(request):
        
        if request.method == "POST":
            
            form = Userloginform(request,data=request.POST) 
            
            if form.is_valid():
                user = form.get_user()
                
                login(request,user)
                
                if user.is_superuser:
                    return redirect('admin_dashboard')
                
                role = user.profile.role
                
                if role == 'doctor':
                    return redirect('doctor_dashboard')
                
                elif role == 'patient':
                    return redirect('patient_dashboard')
                
                logout(request)
                messages.error(request,'invalid User role')
        else:
            form = Userloginform()
                
        return render(request,'accounts/login_page.html',{'form':form})
                
@login_required                
def admin_dashboard(request):
    return render(request,"accounts/admin.html")

@login_required 
def user_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect('login_page')
    return redirect('accounts/admin.html')