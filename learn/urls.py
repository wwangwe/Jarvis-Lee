from django.urls import path
from . import views

app_name = 'learn'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('tests/', views.TestsView.as_view(), name='tests'),
    path('notes/', views.NotesView.as_view(), name='notes'),
    path('tests/mathematics/', views.MathTestsView.as_view(), name='math_tests'),
    path('tests/science/', views.ScienceTestsView.as_view(), name='science_tests'),
    path('tests/english/', views.EnglishTestsView.as_view(), name='english_tests'),
    path('tests/kiswahili/', views.KiswahiliTestsView.as_view(), name='kiswahili_tests'),
    path('tests/social/', views.SocialTestsView.as_view(), name='social_tests'),
    path('tests/religion/', views.ReligionTestsView.as_view(), name='religion_tests'),
    path('notes/mathematics/', views.MathNotesView.as_view(), name='math_notes'),
    path('notes/science/', views.ScienceNotesView.as_view(), name='science_notes'),
    path('notes/english/', views.EnglishNotesView.as_view(), name='english_notes'),
    path('notes/kiswahili/', views.KiswahiliNotesView.as_view(), name='kiswahili_notes'),
    path('notes/social/', views.SocialTestNotes.as_view(), name='social_notes'),
    path('notes/religion/', views.ReligionNotesView.as_view(), name='religion_notes'),
]