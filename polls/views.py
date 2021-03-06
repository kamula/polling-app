from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Question, choice


# Get questions and display them

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'index.html', context)


# show specific questions and answers
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)

    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    return render(request, 'polls/result.html', {'question': question})


# get question and display results
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
