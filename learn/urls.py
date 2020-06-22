from django.urls import path
from . import views

app_name = 'learn'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('tests/', views.TestsView.as_view(), name='tests'),
    path('notes/', views.NotesView.as_view(), name='notes'),
    path('resources/', views.ResourcesView.as_view(), name='resources'),

]