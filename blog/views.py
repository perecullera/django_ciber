# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

from blog.models import Post

def index(request):
    latest_post_list = Post.objects.order_by('-data_pub')[:5]
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'latest_post_list': latest_post_list,
    })
    return HttpResponse(template.render(context))