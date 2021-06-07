from django.shortcuts import render

# Create your views here.
from quiz.models import Question
def qpage(request):
	questions = Question.objects.all()
	return render(request, 'quiz.html', { 'questions': questions})
