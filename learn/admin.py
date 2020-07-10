from django.contrib import admin
from .models import Subject, Question, Choice, Exam


class SubjectAdmin(admin.ModelAdmin):
    fields = ['name']

admin.site.register(Subject, SubjectAdmin)


# class ChoiceAdmin(admin.ModelAdmin):
#     fields = ['choice_text', 'is_correct']

# admin.site.register(Choice, ChoiceAdmin)


class ChoiceInline(admin.TabularInline):
    model = Choice

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('exam', 'question_text')
    list_filter = ['exam']
    search_fields = ['question_text']
    fieldsets = [
        ('Question Information', {'fields': ['exam']}),
        ('Question', {'fields': ['question_text']})
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)

class QuestionInline(admin.StackedInline):
    model = Question

class ExamAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'score')
    list_filter = ['subject']
    fieldsets = [
        ('Exam Information', {'fields':['name', 'subject', 'score']})
    ]
    inlines = [QuestionInline]

admin.site.register(Exam, ExamAdmin)