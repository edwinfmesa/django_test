#from django.template.loader import get_template
#from django.template import Context
#from django.http import HttpResponse

#from index.models import Comment

from django.shortcuts import render_to_response

#import datetime

def home(request):
    return render_to_response('home.html', None)

def mostrar(request):
    return render_to_response('prueba.html', None)

