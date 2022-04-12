from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path("", views.index, name='Home'),
    path("home", views.index, name='Home'),
    path("about", views.about, name='about'),
    path("feedback", views.feedback, name='feedback'),
    path("paid_courses", views.paid_courses, name='paid_courses')
]