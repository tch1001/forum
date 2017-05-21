from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    if(not request.session.has_key('username')):
        return HttpResponseRedirect('/')

    return HttpResponse("here's your dear cat home")