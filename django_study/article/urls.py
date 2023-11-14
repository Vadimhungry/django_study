from django.urls import path

from django_study.article import views

urlpatterns = [
    path('', views.index),
]