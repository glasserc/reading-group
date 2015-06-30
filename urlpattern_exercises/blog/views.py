from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    """show the most recent posts"""
    return HttpResponse('Most recent posts')

def month(request, year, month):
    """show the posts from e.g. 2015-06"""
    return HttpResponse('Posts for {year}-{month}'.format(
        year=year, month=month))

def post(request, post_id):
    """show just the post identified by the ID"""
    return HttpResponse('Post {}'.format(post_id))
