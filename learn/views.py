from django.http import HttpResponse
from django.shortcuts import render
from .models import Subject, Test

def homeView(request):
    subjects = Subject.objects.all()
    return render(request, 'learn/base.html', {'subjects': subjects})

def mathView(request):
    return HttpResponse("Mathematics")

def scienceView(request):
    return HttpResponse("Science")

def englishView(request):
    return HttpResponse("English")

def kiswahiliView(request):
    return HttpResponse("Kiswahili")

def socialView(request):
    return HttpResponse("Social Studies")

def religionView(request):
    return HttpResponse("Religion")

