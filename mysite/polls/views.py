from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse
from .models import Question
from django.template import loader


def index(request):
    return HttpResponse("Hello World, You are at polls index")


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request,'polls/detail.html',{'question': question})


def results(request, question_id):
    response = "Youre looking at th results question %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You are voting on question %s" %
        question_id)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list':
               latest_question_list}
    return render(request, 'polls/index.html', context)
