from django.db import models
from django import forms


class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    a1 = models.IntegerField(default=0)
    a2 = models.IntegerField(default=0)
    a3 = models.IntegerField(default=0)
    a4 = models.IntegerField(default=0)
    a5 = models.IntegerField(default=0)
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject


class Answer(forms.Form):
    answer = forms.IntegerField()

