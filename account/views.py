# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse

def user_login(request):
    return HttpResponse("hello world")