from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.utils.safestring import mark_safe
from django.template import loader
from django.urls import reverse
import json
from .models import GameTicTacToe, GameOthello, GamesList

tictactoe_models = [GameTicTacToe(i) for i in range(7)]
othello_models = [GameOthello(i) for i in range(16)]


def main_page(request):
    list_of_game = GamesList.objects.order_by("-create_date")
    context = {"games": list_of_game}
    return render(request, "games/main.html", context=context)


def othello_lobby(request):
    return render(request, "games/othello/othello_lobby.html")


def othello_ai(request, room_id, player):
    context = {"model": othello_models[room_id], "player": player, "room_id": room_id}
    return render(request, "games/othello/othello_ai.html", context=context)


def othello_player(request, room_id, player):
    context = {"model": othello_models[room_id], "player": player, "room_id": room_id}
    return render(request, "games/othello/othello_player.html", context=context)


def tictactoe(request):
    return render(request, "games/tic-tac-toe/tic-tac-toe_main.html")


def tictactoe_ai(request, room_id):
    model = tictactoe_models[room_id]
    if model.ai:
        if room_id < 2:
            model.play_ai_dumb()
        else:
            model.play_ai_minimax()
        return render(request, "games/tic-tac-toe/tic-tac-toe_player.html", context={"model": model})
    else:
        if request.method == "POST":
            z = int(request.POST.get("action"))
            print(z)
            if z == -2:
                model.initialize()
            else:
                model.update(z)
        return render(request, "games/tic-tac-toe/tic-tac-toe_ai.html", context={"model": model})


def tictactoe_x(request, room_id):
    model = tictactoe_models[room_id]
    if model.turn == 'X':
        if request.method == "POST":
            z = int(request.POST.get("action"))
            print(z)
            if z == -2:
                model.initialize()
            else:
                model.update(z)
            return render(request, "games/tic-tac-toe/tic-tac-toe_waiting.html", context={"model": model})
        else:
            return render(request, "games/tic-tac-toe/tic-tac-toe.html", context={"model": model})
    else:
        return render(request, "games/tic-tac-toe/tic-tac-toe_waiting.html", context={"model": model})


def tictactoe_o(request, room_id):
    model = tictactoe_models[room_id]
    if model.turn == 'O':
        if request.method == "POST":
            z = int(request.POST.get("action"))
            print(z)
            if z == -2:
                model.initialize()
            else:
                model.update(z)
            return render(request, "games/tic-tac-toe/tic-tac-toe_waiting.html", context={"model": model})
        else:
            return render(request, "games/tic-tac-toe/tic-tac-toe.html", context={"model": model})
    else:
        return render(request, "games/tic-tac-toe/tic-tac-toe_waiting.html", context={"model": model})


def ganz(request):
    return render(request, "games/ganz-schon-clever/ganz-schon-clever.html")
