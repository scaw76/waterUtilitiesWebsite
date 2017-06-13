from django.conf.urls import url
from . import views

app_name = 'publicnotices'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<notice_id>[0-9]+)/$', views.detail, name='detail'),
]