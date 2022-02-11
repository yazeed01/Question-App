from django.contrib import admin
from .models import *
# Register your models here.

class AnswersInline(admin.TabularInline):
    model = Answers
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswersInline]


admin.site.register(Answers)
admin.site.register(Questions, QuestionAdmin)
admin.site.register(CorrectAnswer)
admin.site.register(Quiz)
admin.site.register(Points)