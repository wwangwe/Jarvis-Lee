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


# Tests
class MathTestsView(generic.ListView):
    template_name = 'learn/math_tests.html'
    context_object_name = 'subject_list'
    
    def get_queryset(self):
        return Subject.objects.all()


class ScienceTestsView(generic.ListView):
    template_name = 'learn/science_tests.html'
    context_object_name = 'subject_list'
    
    def get_queryset(self):
        return HttpResponse("Science")


class EnglishTestsView(generic.ListView):
    template_name = 'learn/english_tests.html'
    context_object_name = 'subject_list'
    
    def get_queryset(self):
        return HttpResponse("English")


class KiswahiliTestsView(generic.ListView):
    template_name = 'learn/kiswahili_tests.html'
    context_object_name = 'subject_list'
    
    def get_queryset(self):
        return HttpResponse("Kiswahili")


class SocialTestsView(generic.ListView):
    template_name = 'learn/social_tests.html'
    context_object_name = 'subject_list'
    
    def get_queryset(self):
        return HttpResponse("Social")


class ReligionTestsView(generic.ListView):
    template_name = 'learn/religion_tests.html'
    context_object_name = 'subject_list'
    
    def get_queryset(self):
        return HttpResponse("Religion")


# Notes
class MathNotesView(generic.ListView):
    template_name = 'learn/math_notes.html'
    context_object_name = 'subject_list'
    
    def get_queryset(self):
        return HttpResponse("Math")


class ScienceNotesView(generic.ListView):
    template_name = 'learn/science_notes.html'
    context_object_name = 'subject_list'
    
    def get_queryset(self):
        return HttpResponse("Science")


class EnglishNotesView(generic.ListView):
    template_name = 'learn/english_notes.html'
    context_object_name = 'subject_list'
    
    def get_queryset(self):
        return HttpResponse("English")


class KiswahiliNotesView(generic.ListView):
    template_name = 'learn/kiswahili_notes.html'
    context_object_name = 'subject_list'
    
    def get_queryset(self):
        return HttpResponse("Kiswahili")


class SocialTestNotes(generic.ListView):
    template_name = 'learn/social_notes.html'
    context_object_name = 'subject_list'
    
    def get_queryset(self):
        return HttpResponse("Social")


class ReligionNotesView(generic.ListView):
    template_name = 'learn/religion_notes.html'
    context_object_name = 'subject_list'
    
    def get_queryset(self):
        return HttpResponse("Religion")
