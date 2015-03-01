from django.conf.urls import patterns, url
from portfolio import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)