from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^session_words$', views.index),
    url(r'^session_words/process$', views.process),
    #url(r'^session_words/addword$', views.addword),
    url(r'^session_words/clear$', views.clear),
]