from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.list_posts, name='list_posts'),
    url(r'^(?P<post_id>[0-9]+)$', views.show_post, name='show_post'),
    url(r'^comments$', views.list_comments, name='list_comments'),
    url(r'^comments/(?P<comment_id>[0-9]+)$', views.show_comment, name='show_comment'),
]
