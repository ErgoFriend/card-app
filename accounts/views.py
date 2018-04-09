from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login
from .forms import RegisterForm, LoginForm
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
 
class TopPageView(generic.TemplateView):
    template_name = "iniita/index.html"
 
 
class MyPageView(LoginRequiredMixin, generic.TemplateView):
    template_name = "accounts/info.html"
 
 
class CreateUserView(generic.CreateView):
    template_name = 'accounts/create.html'
    form_class = RegisterForm
    success_url = reverse_lazy('accounts:index')

def authlogin(request,user_name,user_password):
    user = authenticate(request,username=user_name,password=user_password)
    if user is not None:
        login(request,user)
        return redirect('/iniita/')
    else:
        return redirect('/iniita/accounts/login')

def logins(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        user_password = request.POST['password']
        if 'sign_btn' in request.POST:
            user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password'],
            ) 
            user.save()
            return authlogin(request,user_name,user_password)
        if 'login_btn' in request.POST:
            return authlogin(request,user_name,user_password)
    return render(request,'accounts/login.html')