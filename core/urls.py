from django.conf.urls import url, include
from core import views


urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^video/(?P<pk>[0-9]+)/$', views.VideoDetailView.as_view(), name='video-detail'),
    url(r'^video/upload/$', views.VideoCreate.as_view(), name='video-upload'),
]