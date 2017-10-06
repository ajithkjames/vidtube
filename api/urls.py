from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from api.views import VideoViewSet, CommentViewSet, CommentList

router = routers.DefaultRouter()
router.register(r'videos', VideoViewSet, 'videos')
# router.register(r'comments', CommentViewSet, 'comments')

urlpatterns = [
	url('^comments/$', CommentList.as_view()),
]

urlpatterns += router.urls