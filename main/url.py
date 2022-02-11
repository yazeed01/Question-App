from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('quiz/<int:qu_id>/', views.quiz, name='quiz'),
    path('success/', views.success, name='success'),
]
