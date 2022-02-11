from msilib import Table
from tkinter.messagebox import NO
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Questions, Answers, CorrectAnswer, Quiz, Points



from .forms import CorrectAnswerForm

from datetime import datetime
# Create your views here.

@login_required
def index(request):
    quizs = Quiz.objects.all()
    if request.user.is_authenticated:

        users  = User.objects.all()
        
        li_users = []
        li_points = []
        
        for i in users:
            po =  Points.objects.filter(correct_answer_point__created_by=i, correct_answer_point__correct_answer__is_correct=True)
            if po:
                li_users.append(str(i.username))
            to_pos = 0
            for p in po:
                to_pos = to_pos + p.proints
            li_points.append(to_pos)

    else:
        ans = None
        li_points = None
        li_users = None
    
    context = {
        'quizs':quizs,
        'li_users':li_users,
        'li_points':li_points,
    }
    return render(request, 'main/index.html',context)


def quiz(request, qu_id):
    ques= get_object_or_404(Questions, pk=qu_id)
    if request.user.is_authenticated:
        
        try:
            ans = CorrectAnswer.objects.get(correct_answer__question=qu_id,created_by=request.user)
            if ans:
                ans = False
        except:
            ans = True
        
        if request.POST.get('flexRadioDefault'):
            an = Answers.objects.get(id=request.POST.get('flexRadioDefault'))
    
        if request.method == "POST":
            form = CorrectAnswerForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.correct_answer = an
                post.created_by = request.user
                post.save()
                print(post.id)
    
                order, created = Points.objects.get_or_create(correct_answer_point__created_by=request.user,correct_answer_point=post,proints=5)

                return redirect('main:success')
        else:
            form = CorrectAnswerForm()
    
    context = {'ques':ques,'ans':ans}
    return render(request, 'main/quiz.html',context)


def success(request):
    return render(request, 'main/success.html')


def administration(request):
    quizs = Quiz.objects.all()
    
    context = {
    'quizs':quizs,
    }
    return render(request, 'admincomp/administration.html',context)

def administration_quiz(request,qu_adm_id):
    # ques= get_object_or_404(Questions, quiz=qu_adm_id)
    que= Questions.objects.get(quiz_id=qu_adm_id)

    # Get All for show in Table.
    coAns = CorrectAnswer.objects.filter(correct_answer__question__quiz=qu_adm_id)
    
    # Get just for correct answer 'True'
    coAns_true = CorrectAnswer.objects.filter(correct_answer__question__quiz=qu_adm_id, correct_answer__is_correct=True)

    import random
    if coAns_true:
        random_coAns = random.choice(coAns_true)
    else:
        random_coAns = None
    context = {
        'coAns':coAns,
        'que':que,
        'random_coAns':random_coAns
    }
    return render(request, 'admincomp/administration_quiz.html', context)