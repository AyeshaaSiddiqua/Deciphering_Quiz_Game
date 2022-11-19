from django.db import models

# Create your models here.

class Easy(models.Model):
    #def __str__(self):
        #return self.question
    question = models.CharField(max_length=500)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    hint = models.CharField(max_length=300)
    answer = models.CharField(max_length=100)

class Medium(models.Model):
    question = models.CharField(max_length=500)
    option1 = models.CharField(max_length=100) 
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    hint = models.CharField(max_length=300)
    answer = models.CharField(max_length=100)

class Difficult(models.Model):
    question = models.CharField(max_length=500)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    hint = models.CharField(max_length=300)
    answer = models.CharField(max_length=100)

class Team_A(models.Model): 
    question_A = models.CharField(max_length=500)
    option1_A = models.CharField(max_length=100)
    option2_A = models.CharField(max_length=100)
    option3_A = models.CharField(max_length=100)
    option4_A = models.CharField(max_length=100)
    hint_A = models.CharField(max_length=300)
    answer_A = models.CharField(max_length=100)

class Team_B(models.Model):
    question_B = models.CharField(max_length=500)
    option1_B = models.CharField(max_length=100)
    option2_B = models.CharField(max_length=100)
    option3_B = models.CharField(max_length=100)
    option4_B = models.CharField(max_length=100)
    hint_B = models.CharField(max_length=300)
    answer_B = models.CharField(max_length=100)
