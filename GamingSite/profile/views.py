from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect


def main_page(request):
    return render(request, "profile/main.html")
