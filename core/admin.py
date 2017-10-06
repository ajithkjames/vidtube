# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from core.models import Category, Video, Comment, Like, Dislike

# Register your models here.
admin.site.register(Category)
admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Dislike)