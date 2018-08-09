from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<transcript_id>[0-9]+)$', views.show, name='show_transcript'),
]
