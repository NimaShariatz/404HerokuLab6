from django.db import models

from django.db import models

class Question(models.Model): #******one question can have many choices
    question_text = models.CharField(max_length=200) #sql field 1
    pub_date = models.DateTimeField('date published') #sql field 2
    
    
class Choice(models.Model): #******but one choice can only have one question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)