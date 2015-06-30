from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Main entry point for Games People Play site.
    # At present we only have one game, plus a news feed and a polls
    # application that Freddy found online. We're going to add more
    # games later.
    #
    # This is for the tic-tac-toe part of the site.
    url(r'play', include('tictactoe.urls')),

    # Original name for the blog was "The logs"
    url(r'^logger/', include('blog.urls')),
    # Our SEO consultant recommended that our URLs have "thoughts" in
    # the name instead
    url(r'^thoughts', include('blog.urls')),

    # Polls
    url(r'^voting/', include('polls.urls')),

    # Of course, administrative functions are in the usual place
    url(r'^admin/', include(admin.site.urls)),
]
