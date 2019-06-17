from django.shortcuts import render
from .models import Question
from django.shortcuts import get_object_or_404

def index(request):
    latest_question_list = Question.objects.order_by('-published_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
   question = get_object_or_404(Question, pk=question_id)
   return(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
    response = "You are looking at the results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting at question %s" % question_id)