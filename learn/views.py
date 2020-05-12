from django.shortcuts import render

def landingPage(request):
    return render(request, 'learn/home.html')

def aboutPage(request):
    return render(request, 'learn/about.html')
