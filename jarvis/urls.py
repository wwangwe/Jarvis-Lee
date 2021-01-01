"""
jarvis URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('quiz/', include('quizzes.urls')),
    path('nested_admin/', include('nested_admin.urls')),
]
