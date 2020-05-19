from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name='index'),
    path('mathematics', views.mathView, name='mathematics'),
    path('science', views.scienceView, name='science'),
    path('english', views.englishView, name='english'),
    path('kiswahili', views.kiswahiliView, name='kiswahili'),
    path('social', views.socialView, name='social'),
    path('religion', views.religionView, name='religion'),
]