from django.db import models


class Subject(models.Model):
    name          = models.CharField(max_length = 20)
    symbol        = models.CharField(max_length = 5)

    def __str__(self):
        return "%s" % (self.name)
    

class Test(models.Model):
    test_number    = models.CharField(max_length = 25, null = True)
    subject        = models.ForeignKey(Subject,on_delete=models.CASCADE)
    max_score      = models.IntegerField()
    
    class Meta:
        order_with_respect_to = 'subject'

    def __str__(self):
        return "%s" % (self.subject.name)


class Question(models.Model):
    test            = models.ForeignKey(Test, null = True, on_delete = models.CASCADE)
    question_text   = models.CharField(max_length = 255, null = True)

    class Meta:
        order_with_respect_to = 'test'

    def __str__(self):
        return "%s %s" % (self.test, self.question_text)

class Answer(models.Model):
    question        = models.ForeignKey(Question, on_delete = models.CASCADE, related_name = "Answers")
    answer_text     = models.CharField(max_length = 255, null = True)
    is_correct      = models.NullBooleanField(default = None)

    class Meta:
        order_with_respect_to   = 'question'
        unique_together         = ('question', 'is_correct',)
        
