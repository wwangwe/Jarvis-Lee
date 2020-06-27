from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import Subject, Test, Question, Answer


class  IndexView(generic.ListView):
    template_name = 'learn/index.html'
    context_object_name = 'subject_list'
    
    def get_queryset(self):
        return Subject.objects.all()


class TestsView(generic.ListView):
    template_name = 'learn/tests.html'
    context_object_name = 'subject_list'
    
    def get_queryset(self):
        return Subject.objects.all()


class NotesView(generic.ListView):
    template_name = 'learn/notes.html'
    context_object_name = 'subject_list'
    
    def get_queryset(self):
        return Subject.objects.all()
    

class ResourcesView(generic.ListView):
    template_name = 'learn/resources.html'
    context_object_name = 'subject_list'
    
    def get_queryset(self):
        return Subject.objects.all()


