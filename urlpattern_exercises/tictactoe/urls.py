from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'(?P<game_id>[0-9]+)', views.game),
]
