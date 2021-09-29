from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.


def index(req: HttpRequest):
    return HttpResponse("Hello World. You are at the poll's index.")
