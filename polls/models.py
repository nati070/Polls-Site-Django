import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')

    #make a overide to change the name object to question text
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)

class Choice(models.Model):
    question = models.ForeignKey   
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    #make a overide to change the name object to choise text
    def __str__(self):
        return self.choice_text



