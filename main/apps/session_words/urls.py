from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add/word', views.addWord),
    url(r'^clear', views.clear),
]
