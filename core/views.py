# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, reverse
from django.views.generic import TemplateView
from django.views import generic
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from core.models import Video

# Create your views here.
class HomeView(LoginRequiredMixin, TemplateView):
	template_name= 'home.html'


class VideoDetailView(DetailView):

    model = Video

    def get_context_data(self, **kwargs):
        context = super(VideoDetailView, self).get_context_data(**kwargs)
        return context


class VideoCreate(CreateView):
    model = Video
    fields = ['title','description','category','file','thumbnail']

    def form_valid(self, form):
        form.instance.uploader = self.request.user
        return super(VideoCreate, self).form_valid(form)

    def get_success_url(self):
            return reverse('video-detail', kwargs={'pk': self.object.id})