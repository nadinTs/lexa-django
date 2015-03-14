from django.conf.urls import patterns, url
from portfolio import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<category_nick>\w+)/$', views.category_index, name="category_index"),
    url(r'^(?P<category_nick>\w+)/(?P<project_nick>\w+)', views.project_details, name="project_details"),
    url(r'^base$', views.base, name='base')
)