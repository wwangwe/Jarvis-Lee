from django.db import models
from django.core.validators import MaxLengthValidator
class Subject(models.Model):
    name = models.CharField(max_length = 20)
    symbol = models.CharField(max_length = 5)

    def __str__(self):
        return "%s" % (self.name)
    
class Test(models.Model):
    test_number = models.CharField(max_length = 25, null = True)
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE
    )
    score = models.IntegerField()
    
    def __str__(self):
        return "%s" % (self.subject.name)

class Question(models.Model):
    test = models.ForeignKey(
        Test,
        null = True,
        # default = "Some Test",
        on_delete = models.CASCADE
    )
    question_text = models.CharField(max_length = 255, null = True)
    choice_a      = models.CharField(max_length = 25, null = True)
    choice_b      = models.CharField(max_length = 25, null = True)
    choice_c      = models.CharField(max_length = 25, null = True)
    choice_d      = models.CharField(max_length = 25, null = True)

    def __str__(self):
        return "%s %s %s %s %s %s" % (
            self.test, 
            self.question_text, 
            self.choice_a, 
            self.choice_b, 
            self.choice_c, 
            self.choice_d
        )

class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete = models.CASCADE,
    )
    solution = models.CharField(max_length = 10)