from django.forms import ModelForm
from .models import Answers , CorrectAnswer
from django import forms

class CorrectAnswerForm(ModelForm):
    
    class Meta:
            model = CorrectAnswer
            exclude = ['correct_answer','created_by']