from django.db import models


class Subject(models.Model):
    name          = models.CharField(max_length = 20)

    def __str__(self):
        return self.name
class Exam(models.Model):
    name           = models.CharField(max_length=20)
    subject        = models.ForeignKey(Subject,on_delete=models.CASCADE)

    class Meta:
        order_with_respect_to = 'name'

    def __str__(self):
        return self.name


class Question(models.Model):
    exam           = models.ForeignKey(Exam, on_delete=models.CASCADE)
    subject        = models.ForeignKey(Subject,on_delete=models.CASCADE)
    max_score      = models.IntegerField(default=100)
    question_text   = models.TextField(max_length = 255, null = False)

    class Meta:
        order_with_respect_to = 'exam'

    def __str__(self):
        return "%s" % (self.question_text)


class Choice(models.Model):
    question        = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text     = models.CharField(max_length = 255, null = False)
    is_correct      = models.NullBooleanField(default = None)

    class Meta:
        order_with_respect_to   = 'question'
        unique_together         = ('question', 'is_correct',)
    
    def __str__(self):
        return self.choice_text