from django import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def apptwo(request):
    return HttpResponse('App two created')

def picture_detail(request):
    template = loader.get_template('apptwo/index.html')
    return HttpResponse(template.render({}, request))