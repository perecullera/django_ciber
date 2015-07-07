# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from blog import models

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

