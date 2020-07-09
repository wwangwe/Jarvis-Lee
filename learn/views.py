from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from django.core.paginator import Paginator

from .models import Subject, Question, Choice


class BaseView(generic.ListView):
    template_name = 'learn/base.html'
    context_object_name = 'subject_list'

    def get_queryset(self):
        return Subject.objects.all()


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
def math_tests(request):
    quest_list = Question.objects.all()
    quest_length = len(quest_list)

    page = request.GET.get('page', 1)
    paginator = Paginator(quest_list, 1)

    try:
        quest = paginator.page(page)
    
    except PageNotAnInteger:
        quest = paginator.page(1)

    except EmptyPage:
        quest = paginator.page(paginator.num_pages)
    
    return render(request, 'learn/math_tests.html', {'quest': quest, 'quest_length': quest_length}) 


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