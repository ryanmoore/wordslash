from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<num_hands>\d+)/(?P<seed>[\d\w]+)$', views.game, name='game'),
]
