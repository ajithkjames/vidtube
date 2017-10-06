# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from account.forms import CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication
from account.models import User
from account.serializers import UserSerializer
from account.permissions import UserPermissions


class UserViewSet(viewsets.ModelViewSet):
	"""User API view"""
 
	serializer_class = UserSerializer
	queryset = User.objects.all()
	permission_classes = (UserPermissions,)


class profileView(APIView):

    serializer_class = UserSerializer

    def get(self, request, format=None):

        user = User.objects.get(pk=self.request.user.id)
        data = self.serializer_class(user)
        return Response(data.data)

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})