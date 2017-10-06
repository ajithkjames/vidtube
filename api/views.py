# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from api.serializers import VideoSerializer, CommentSerializer
from core.models import Video, Comment


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page'


class VideoViewSet(viewsets.ModelViewSet):
	"""Video API view"""

	serializer_class = VideoSerializer
	queryset = Video.objects.all().order_by('-created_at')

class CommentViewSet(viewsets.ModelViewSet):
	"""comment API view"""

	serializer_class = CommentSerializer
	queryset = Comment.objects.all().order_by('-created_at')


class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    pagination_class = None

    def get_queryset(self):
        queryset = Comment.objects.all()
        video = self.request.query_params.get('video', None)
        if video is not None:
            queryset = queryset.filter(video=video).order_by('-created_at')
        return queryset

    def perform_create(self, serializer):
    	serializer.save(author=self.request.user)