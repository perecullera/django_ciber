# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

from blog.models import Post

def index(request):
    latest_post_list = Post.objects.order_by('-data_pub')[:5]
    most_three_visited = Post.objects.order_by('-visits')[:3]
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'latest_post_list': latest_post_list,
        'most_three_visited':most_three_visited
            })
    return HttpResponse(template.render(context))

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.visits +=1
    post.save()
    most_three_visited = Post.objects.order_by('-visits')[:3]

    return render(request, 'detail.html', {'post': post,
    	'most_three_visited':most_three_visited})