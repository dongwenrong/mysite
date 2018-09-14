# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','birth','phone',)
    list_filter = ("phone",)
    #search_fields = ("phone",)
admin.site.register(UserProfile,UserProfileAdmin)