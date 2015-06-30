from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<year>[0-9]+)/(?P<month>[0-9]+)/$', views.month),
    url(r'^(?P<post_id>[0-9]+)/$', views.post),
    # Our SEO expert recommends that our posts include their title in
    # the URLs
    url(r'^(?P<post_id>[0-9]+)-.*/$', views.post),
]
