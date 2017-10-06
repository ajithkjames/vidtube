from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views
from account.forms import LoginForm

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login$', views.login, {'template_name': 'login.html', 
	'authentication_form': LoginForm,
	'redirect_authenticated_user': True},name='login'),
    url(r'^logout', views.logout, {'next_page': 'login'},name='logout'),
    url(r'^', include('core.urls')),
    url(r'^', include('account.urls')),
    url(r'^api/', include('api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)