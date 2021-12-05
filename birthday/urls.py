from django.urls import path
from birthday import views

urlpatterns = [
    path('birthday/', views.BirthdayByDate.as_view()),
]