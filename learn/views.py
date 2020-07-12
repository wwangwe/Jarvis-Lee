from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Exam, Question, Subject, Choice


class  IndexView(ListView):
    template_name = 'learn/index.html'
    context_object_name = 'subject_list'
    
    def get_queryset(self):
        return Subject.objects.all()


class ExamListView(ListView):
    template_name = 'learn/list/exam_list.html'
    context_object_name = 'subject_list'
    
    def get_queryset(self):
        return Subject.objects.all()


class NotesListView(ListView):
    template_name = 'learn/list/notes_list.html'
    context_object_name = 'subject_list'
    
    def get_queryset(self):
        return Subject.objects.all()


def MathExamView(request, pk):
    exam = get_object_or_404(Exam, pk=pk)    
    quest_list = exam.question_set.all()
    quest_length = len(quest_list)
    page = request.GET.get('question', 1)
    paginator = Paginator(quest_list, 1)

    try:
        quest = paginator.page(page)

    except PageNotAnInteger:
        quest = paginator.page(1)

    except EmptyPage:
        quest = paginator.page(paginator.num_pages)
    
    question = get_object_or_404(Question, pk=page)
    choice_list = question.choice_set.all()

    return render(request, 'learn/exams/math.html',
        {
        'quest': quest, 
        'quest_length': quest_length,
        'choice': choice_list
        }) 


def ScienceExamsView(request, pk):
    exam = get_object_or_404(Exam, pk=pk)    
    quest_list = exam.question_set.all()
    quest_length = len(quest_list)
    page = request.GET.get('question', 1)
    paginator = Paginator(quest_list, 1)

    try:
        quest = paginator.page(page)

    except PageNotAnInteger:
        quest = paginator.page(1)

    except EmptyPage:
        quest = paginator.page(paginator.num_pages)
    
    question = get_object_or_404(Question, pk=page)
    choice_list = question.choice_set.all()

    return render(request, 'learn/exams/math.html',
        {
        'quest': quest, 
        'quest_length': quest_length,
        'choice': choice_list
        }) 

