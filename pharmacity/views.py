from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader

# Create your views here.

def index(request):
    template = loader.get_template('pharmacity/index.htm')
    context = {}
    return HttpResponse(template.render(context, request))

def signup_user(request):
    pass

def signup_phamacist(request):
    pass

def login_user(request):
    pass

def login_pharmacist(request):
    pass

def logout(request):
    pass
