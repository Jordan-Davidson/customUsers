from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from courier.settings import AUTH_USER_MODEL

from customUsers.forms import LoginForm, SignupForm
from customUsers.models import CustomUser
# Create your views here.

@login_required
def index(request):
    html = 'index.html'
    data = AUTH_USER_MODEL
    return render(request, html, {'data': data})

def loginview(request):
    html = 'signup.html'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage')))
    form = LoginForm()
    return render(request, html, {'form': form})


def signup(request):
    html = 'signup.html'
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = CustomUser.objects.create_user(
                username=data['username'],
                displayname=data['displayname'],
                password=data['password']
            )
            if user:
                login(request,user)
                return HttpResponseRedirect(
                request.GET.get('next', reverse('homepage')))
            return HttpResponseRedirect(reverse('homepage'))
    form = SignupForm()
    return render(request, html, {'form':form})