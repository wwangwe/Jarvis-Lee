from django.contrib import admin
from .models import Subject, Question, Choice, Exam


class SubjectAdmin(admin.ModelAdmin):
    fields = ['name']

admin.site.register(Subject, SubjectAdmin)


class ChoiceAdmin(admin.ModelAdmin):
    fields = ['choice_text', 'is_correct']

admin.site.register(Choice, ChoiceAdmin)


class ChoiceInline(admin.TabularInline):
    model = Choice

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('exam', 'subject', 'max_score', 'question_text')
    list_filter = ['subject']
    search_fields = ['question_text']
    fieldsets = [
        ('Question Information', {'fields': ['exam', 'subject', 'max_score']}),
        ('Question', {'fields': ['question_text']})
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 49

class ExamAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject')
    list_filter = ['subject']
    fieldsets = [
        ('Exam Information', {'fields':['name', 'subject']})
    ]
    inlines = [QuestionInline]

admin.site.register(Exam, ExamAdmin)