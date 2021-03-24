from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.urls import reverse_lazy
# Create your views here.

class UserLogin(LoginView):
    template_name = 'userauth/login.html'
    fields='__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')

class UserRegister(FormView):
    template_name ='userauth/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('tasks')

    def form_valid(self,form):
        user =form.save()
        if user is not None:
            login(self.request,user)
        return super(UserRegister,self).form_valid(form)

    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')

        return super(UserRegister,self).get(*args,**kwargs)
