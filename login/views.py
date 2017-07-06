from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from login.models import User
from .forms import LoginForm, SignUpForm
import datetime

# Create your views here.
def login(request):
    print(request.method)
    form = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username =  request.POST.get('username', '')
            password = request.POST.get('password', '')
            try:
                User.objects.get(username = username, password = password)
                request.session['username'] = username
            except User.DoesNotExist:
                try:
                    User.objects.get(email=username, password=password)
                    request.session['username'] = username
                except User.DoesNotExist:
                    return render(request, 'login.html', {'form': LoginForm(), 'failed': True})


            response = HttpResponseRedirect('/home/')
            return response
    else:
        if request.session.has_key('username'):
            username = request.session['username']
            print(username)
            return HttpResponseRedirect('/home/')
        form = LoginForm()
    return render(request, 'login.html', {'form': form, 'failed': False})

def signout(request):
    del request.session['username']
    return HttpResponseRedirect('/')
def register(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            email = request.POST.get('email', '')
            password = request.POST.get('password', '')
            cfmPassword = request.POST.get('cfmPassword', '')
            if password != cfmPassword:
                    return render(request, 'register.html', {'form': form, 'failed': 1})

            # print(username, email, password)
            try:
                User.objects.get(username = username)
                return render(request, 'register.html', {'form': form, 'failed':2})
            except User.DoesNotExist:
                addUser = User(username=username, email=email, password = password)
                addUser.save()
                return HttpResponse(render(request, 'accountCreated.html'))

    return render(request, 'register.html', {'form': form, 'failed': 0})

def users(reqeust):
    return HttpResponse("<h1>hi! oops sorry, under development :3</h1>")