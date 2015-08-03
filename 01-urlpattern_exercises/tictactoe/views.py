from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    """show the most recent games"""
    return HttpResponse('Most recent games')

def game(request, game_id):
    """show just the game identified by the ID"""
    return HttpResponse('game {}'.format(game_id))

def games_for_me(request):
    """show the games for the current user"""
    return HttpResponse('My open games')

def games_for_player(request, player_name):
    """show the games that a player is playing in"""
    return HttpResponse('Games for {}'.format(player_name))
