from django.contrib import admin
from .models import Subject, Test, Question, Answer

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol')

admin.site.register(Subject, SubjectAdmin)

class TestAdmin(admin.ModelAdmin):
    list_display = ('test_number','subject', 'max_score')

admin.site.register(Test, TestAdmin)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('test', 'question_text')

admin.site.register(Question, QuestionAdmin)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer_text', 'is_correct')

admin.site.register(Answer, AnswerAdmin)

