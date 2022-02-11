from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('quiz/<int:qu_id>/', views.quiz, name='quiz'),
    path('success/', views.success, name='success'),
    path('administration/', views.administration, name='administration'),
    path('administration/quiz/<int:qu_adm_id>/', views.administration_quiz, name='administration_quiz'),
]
