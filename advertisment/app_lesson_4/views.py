from django.shortcuts import render
from django.http import HttpResponse


def lesson(request):
    return HttpResponse('<h1>Домашка по 4 занятию</h1>')
# Create your views here.
