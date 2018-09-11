# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import BlogArticles

def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request,"blog/titles.html",{"blogs":blogs})
