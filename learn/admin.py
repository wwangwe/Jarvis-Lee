from django.contrib import admin
from .models import Subject, Test, Question

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol')

admin.site.register(Subject, SubjectAdmin)

class TestAdmin(admin.ModelAdmin):
    list_display = ('subject', 'score')

admin.site.register(Test, TestAdmin)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'choice_a', 'choice_b', 'choice_c', 'choice_d')

admin.site.register(Question, QuestionAdmin)



