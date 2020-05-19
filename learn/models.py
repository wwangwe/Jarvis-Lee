from django.db import models
from django.core.validators import MaxLengthValidator
class Subject(models.Model):
    name = models.CharField(max_length = 20)
    symbol = models.CharField(max_length = 5)
    
class Test(models.Model):
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE
    )
    score = models.IntegerField(
        validators=[
            MaxLengthValidator(100)
        ]
    )
    def __unicode__(self):
        return u"%  s" %self.subject

class Question(models.Model):
    question_text = models.CharField(max_length = 255)
    choice_a = models.CharField(max_length = 255)
    choice_b = models.CharField(max_length = 255)
    choice_c = models.CharField(max_length = 255)
    choice_d = models.CharField(max_length = 255)
    
    CHOICES = [
        (choice_a, "A"),
        (choice_b, "B"),
        (choice_c, "C"),
        (choice_d, "D")
    ]
    solution = models.CharField(
        default = choice_a,
        choices = CHOICES,
        max_length = 2,
    )
