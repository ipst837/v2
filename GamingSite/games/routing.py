from django.urls import re_path
from .consumer import *


websocket_urlpatterns = [
    re_path(r"ws/games/othello/$", OthelloLobby.as_asgi()),
    re_path(r"ws/games/othello/(?P<room_id>\d+)/(?P<player>\w+)/$", OthelloDuel.as_asgi()),
    re_path(r"ws/games/othello/ai/(?P<room_id>\d+)/(?P<player>\w+)/$", OthelloAI.as_asgi()),
]
