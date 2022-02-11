
from django.db import models
from django.contrib.auth.models import User
from django.forms import DateField

# Create your models here.

class Quiz(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    date_start = models.DateField()
    date_end = models.DateField()

class Questions(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    tyep = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def get_answers(self):
        return Answers.objects.filter(question=self)
    
    def __str__(self):
        return self.text

class Answers(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text

class CorrectAnswer(models.Model):
    correct_answer = models.ForeignKey(Answers, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_point(self):
        return Points.objects.filter(correct_answer_point=self)


class Points(models.Model):
    correct_answer_point = models.ForeignKey(CorrectAnswer, on_delete=models.CASCADE)
    proints= models.IntegerField()
