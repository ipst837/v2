from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.template import loader
from django.urls import reverse
from django.utils import timezone


class Menu:
    def __init__(self, name, url):
        self.name = name
        self.url = url


def base(request):
    return render(request, 'base.html')


def main_page(request):
    return render(request, 'main.html')
