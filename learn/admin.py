from django.contrib import admin
from .models import Subject, Test, Question, Answer

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol')

admin.site.register(Subject, SubjectAdmin)

class TestAdmin(admin.ModelAdmin):
    list_display = ('subject', 'score')

admin.site.register(Test, TestAdmin)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('test', 'question_text', 'choice_a', 'choice_b', 'choice_c', 'choice_d')

admin.site.register(Question, QuestionAdmin)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'solution')

admin.site.register(Answer, AnswerAdmin)

