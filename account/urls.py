from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as restview
from account.views import UserViewSet, profileView, signup

router = routers.DefaultRouter()
router.register(r'user', UserViewSet, 'user_detail')


urlpatterns = [

    url(r'^login/', restview.obtain_auth_token),
    url(r'^profile/', profileView.as_view()),
    url(r'^signup/', signup, name='signup'),
]

urlpatterns += router.urls