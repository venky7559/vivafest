from django.shortcuts import render
from app import forms 

from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail

# Create your views here.
def register(request):
    register=False
    if request.method=="POST":
        user_form=forms.User_Form(request.POST)
        user_data_form=forms.Students_form(request.POST,request.FILES)
        d=request.POST.get('email', '')

        #import pdb;pdb.set_trace()
        if user_form.is_valid() and user_data_form.is_valid():
            user=user_form.save(commit=True)
            user.set_password(user.password)
            user.save()

            user_data=user_data_form.save(commit=False)
            user_data.user=user

            if 'profile_pic' in request.FILES:
                user_data.profile_pic=request.FILES['profile_pic']
            user_data.save()
            register=True

            send_mail("Registration Successful","thanku for registering","nelaturiv@gamil.com", [d],fail_silently=False)
    else:
        user_form=forms.User_Form()
        user_data_form=forms.Students_form()
    
    dt={'form':user_data_form,'form_user':user_form,'register':register}
    return render(request,'register.html',context=dt)

def index(request):
    user_name=request.session.get('username',"No User")
    return render(request,'base.html',context={'user_name':user_name})


def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username',"")
        password=request.POST.get('password','')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                request.session['username']=username
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Not an Active user")
        else:
            print("Invalid Login")
            return HttpResponse("Invalid Login")
    else:
        return render(request,'login.html')

@login_required
def user_logout(request):
    logout(request)
    try:
        del request.session['username']
    except:
        pass
    return HttpResponseRedirect(reverse('index'))

@login_required
def wish(request):
    return HttpResponse("<h1>Hai Mr./Ms. {} </h1>".format(request.session['username']))