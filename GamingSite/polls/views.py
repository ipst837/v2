from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.template import loader
from django.urls import reverse
from .models import Question
from django.utils import timezone


def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'polls/question_page.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    z = question.content.split('\r\n')
    context = {'question': question, 'z': z, 'total': question.a1 + question.a2 + question.a3 + question.a4 + question.a5}
    return render(request, 'polls/question_detail.html', context)


def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    q = int(request.POST.get("answer"))
    if q == 1:
        question.a1 += 1
    elif q == 2:
        question.a2 += 1
    elif q == 3:
        question.a3 += 1
    elif q == 4:
        question.a4 += 1
    else:
        question.a5 += 1
    question.save()
    return redirect('polls:detail', question_id=question_id)
