from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import F
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from polls.models import Choice, Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}

    return render(request, "polls/index.html", context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {"question": question}

    return render(request, "polls/detail.html", context)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {"question": question}
    return render(request, "polls/results.html", context)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {"question": question, "error_message": "Você não selecionou uma das escolhas."}
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])

    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            context,
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question_id, )))
