from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    """show the most recent polls"""
    return HttpResponse('Most recent polls')

def poll(request, poll_id):
    """show just the poll identified by the ID"""
    return HttpResponse('poll {}'.format(poll_id))
