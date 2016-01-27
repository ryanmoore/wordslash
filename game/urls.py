from django.conf.urls import url

from . import views

app_name='game'
urlpatterns = [
    url(r'^(?P<num_hands>\d+)/(?P<seed>[\d\w]+)$', views.game, name='play'),
    url(r'^answer/(?P<num_hands>\d+)/(?P<seed>[\d\w]+)$',
        views.answer, name='answer'),
]
