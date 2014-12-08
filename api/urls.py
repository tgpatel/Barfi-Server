from django.conf.urls import patterns, include, url


from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^prediction/$', views.take_action),
]
