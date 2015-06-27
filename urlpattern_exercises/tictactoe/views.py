from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    """show the most recent games"""
    return HttpResponse('Most recent games')

def game(request, game_id):
    """show just the game identified by the ID"""
    return HttpResponse('game {}'.format(game_id))
