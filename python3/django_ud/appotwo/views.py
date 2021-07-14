from django import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def apptwo(request):
    return HttpResponse('App two created')

def picture_detail(request):
    template = loader.get_template('apptwo/index.html')
    context = {'company_name' : {'DjongoCorp Inc'} , 'collaborators': {'James' : 'CEO', 'ED' : 'DO', 'ANNA': 'BIG BOSS'}}
    return HttpResponse(template.render(context, request))