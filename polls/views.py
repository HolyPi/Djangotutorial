from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from datetime import datetime
from django.http import HttpResponse
from django.views import View 

from .models import Question 

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

class ShowTimeView(View):
    def get(self, request):
        now = datetime.now()
        html = "<html><body>It is now {}<body></html>".format(now)
        return HttpResponse(html)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse("You're voting on question %s." % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)