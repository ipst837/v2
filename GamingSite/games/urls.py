from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    path('', views.main_page, name='main'),
    path('othello/', views.othello_lobby, name='othello'),
    path('othello/ai/<int:room_id>/<str:player>/', views.othello_ai, name='othello_ai'),
    path('othello/<int:room_id>/<str:player>/', views.othello_player, name='othello_player'),
    path('tictactoe/', views.tictactoe, name='tictactoe'),
    path('tictactoe/ai/<int:room_id>/', views.tictactoe_ai, name='tictactoe_ai'),
    path('tictactoe/X/<int:room_id>/', views.tictactoe_x, name='tictactoe_X'),
    path('tictactoe/O/<int:room_id>/', views.tictactoe_o, name='tictactoe_O'),
    path('ganz-schon-clever/', views.ganz, name='ganz'),
]
