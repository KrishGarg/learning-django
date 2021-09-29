from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404
from .models import Question

# Create your views here.


def index(req: HttpRequest):
    questions = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": questions}
    return render(req, "polls/index.html", context)


def detail(req: HttpRequest, question_id: int):
    question = get_object_or_404(Question, pk=question_id)
    return render(req, "polls/detail.html", {"question": question})


def results(req: HttpRequest, question_id: int):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response)


def vote(req: HttpRequest, question_id: int):
    return HttpResponse(f"You're voting on question {question_id}.")
