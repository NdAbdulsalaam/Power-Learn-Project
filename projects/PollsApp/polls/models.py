from django.db import models
from django.contrib import admin

import datetime
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("published date")
    
    def __str__(self):
        return self.question_text
    
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently"
    )
    
    def was_published_recently(self):
        now = timezone.now()
        yesterday = now - datetime.timedelta(days=1)
        return yesterday <= self.pub_date <= now
        
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete= models.CASCADE)
    choice_text = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text