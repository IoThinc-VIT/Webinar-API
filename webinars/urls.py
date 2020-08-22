from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('create/view/',views.webinarAdder.as_view()),
    path('update/view/',views.webinarAdder.as_view()),
    path('delete/view/<str:pk>/',views.webinarAdder.as_view()),
]