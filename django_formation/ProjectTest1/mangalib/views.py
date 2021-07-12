from django import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import context, loader
# Create your views here.

def index(request):
    context = {"message" : "Many Men"}
    template = loader.get_template("mangalib/index.html")
    return HttpResponse(template.render(context, request))